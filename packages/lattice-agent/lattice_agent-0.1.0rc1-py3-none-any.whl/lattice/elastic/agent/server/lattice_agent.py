import logging
import os
import shutil
import signal
import tempfile
from typing import Any, Dict, Optional, Tuple

from lattice.elastic.agent.server.api import (
    RunResult,
    SimpleElasticAgent,
    WorkerGroup,
    WorkerSpec,
    WorkerState,
)
from lattice.elastic.utils import macros
from lattice.elastic.multiprocessing import PContext, start_processes

logging.basicConfig(format='[%(levelname)s %(name)s] %(message)s', level=logging.INFO)

class LatticeAgent(SimpleElasticAgent):
    def __init__(
        self,
        spec: WorkerSpec,
        start_method='spawn',
        exit_barrier_timeout: float = 300,
        log_dir: Optional[str] = None,
        extra_env = None,
    ):
        super().__init__(spec, exit_barrier_timeout)
        self._start_method = start_method
        # TODO: Find some way to replace the PContext class
        self._pcontext: Optional[Any] = None
        rdzv_run_id = spec.rdzv_handler.get_run_id()
        self._log_dir = self._make_log_dir(log_dir, rdzv_run_id)
        self._extra_env = extra_env

    def _make_log_dir(self, log_dir: Optional[str], rdzv_run_id: str):
        base_log_dir = log_dir or tempfile.mkdtemp(prefix="torchelastic_")
        os.makedirs(base_log_dir, exist_ok=True)
        dir = tempfile.mkdtemp(prefix=f"{rdzv_run_id}_", dir=base_log_dir)
        logging.info(f"log directory set to: {dir}")
        return dir

    def _start_workers(self, worker_group: WorkerGroup) -> Dict[int, Any]:
        spec = worker_group.spec
        store = worker_group.store
        assert store is not None
        master_addr, master_port = super()._get_master_addr_port(store)
        restart_count = spec.max_restarts - self._remaining_restarts

        # TODO: Likely to be deprecated
        use_agent_store = spec.rdzv_handler.get_backend() == 'static'

        args: Dict[int, Tuple] = {}
        envs: Dict[int, Dict[str, str]] = {}
        for worker in worker_group.workers:
            local_rank = worker.local_rank
            worker_env = {
                "LOCAL_RANK": str(local_rank),
                "RANK": str(worker.global_rank),
                "NODE_RANK": str(worker_group.group_rank),
                "GROUP_RANK": str(worker_group.group_rank),
                "ROLE_RANK": str(worker.role_rank),
                "ROLE_NAME": spec.role,
                "LOCAL_WORLD_SIZE": str(spec.local_world_size),
                "WORLD_SIZE": str(worker.world_size),
                "GROUP_WORLD_SIZE": str(worker_group.group_world_size),
                "ROLE_WORLD_SIZE": str(worker.role_world_size),
                "MASTER_ADDR": master_addr,
                "MASTER_PORT": str(master_port),
                # TODO (JOHN): add this functionality back in
                #"CHECKPOINT_BUCKET": os.environ["CHECKPOINT_BUCKET"],
                #"STEPS_PER_CHECKPOINT": os.environ["STEPS_PER_CHECKPOINT"],
                "TORCHELASTIC_RESTART_COUNT": str(restart_count),
                "TORCHELASTIC_MAX_RESTARTS": str(spec.max_restarts),
                "TORCHELASTIC_RUN_ID": spec.rdzv_handler.get_run_id(),
                "TORCHELASTIC_USE_AGENT_STORE": str(use_agent_store),
                "NCCL_ASYNC_ERROR_HANDLING": str(1),
            }
            if "OMP_NUM_THREADS" in os.environ:
                worker_env["OMP_NUM_THREADS"] = os.environ["OMP_NUM_THREADS"]
            if self._extra_env:
                worker_env.update(self._extra_env)
            envs[local_rank] = worker_env
            worker_args = list(spec.args)
            worker_args = macros.substitute(worker_args, str(local_rank))
            args[local_rank] = tuple(worker_args)

        # scaling events do not count towards restarts (gets same attempt #)
        # remove existing log dir if this restart is due to a scaling event
        attempt_log_dir = os.path.join(self._log_dir, f"attempt_{restart_count}")
        shutil.rmtree(attempt_log_dir, ignore_errors=True)
        os.makedirs(attempt_log_dir)

        assert spec.entrypoint is not None
        self._pcontext = start_processes(
            name=spec.role,
            entrypoint=spec.entrypoint,
            args=args,
            envs=envs,
            log_dir=attempt_log_dir,
            start_method=self._start_method,
            redirects=spec.redirects,
            tee=spec.tee,
        )

        return self._pcontext.pids()

    def _stop_workers(self, worker_group: WorkerGroup) -> None:
        self._shutdown()

    def _monitor_workers(self, worker_group: WorkerGroup) -> RunResult:
        role = worker_group.spec.role
        worker_pids = {w.id for w in worker_group.workers}
        assert self._pcontext is not None
        pc_pids = set(self._pcontext.pids().values())
        if worker_pids != pc_pids:
            logging.error(
                f"[{role}] worker pids do not match process_context pids."
                f" Expected: {worker_pids}, actual: {pc_pids}"
            )
            return RunResult(state=WorkerState.UNKNOWN)

        result = self._pcontext.wait(0)
        if result:
            if result.is_failed():
                # map local rank failure to global rank
                worker_failures = {}
                for local_rank, failure in result.failures.items():
                    worker = worker_group.workers[local_rank]
                    worker_failures[worker.global_rank] = failure
                return RunResult(
                    state=WorkerState.FAILED,
                    failures=worker_failures,
                )
            else:
                # copy ret_val_queue into a map with a global ranks
                workers_ret_vals = {}
                for local_rank, ret_val in result.return_values.items():
                    worker = worker_group.workers[local_rank]
                    workers_ret_vals[worker.global_rank] = ret_val
                return RunResult(
                    state=WorkerState.SUCCEEDED,
                    return_values=workers_ret_vals,
                )
        else:
            return RunResult(state=WorkerState.HEALTHY)
    
    def _shutdown(self, death_sig: signal.Signals = signal.SIGTERM) -> None:
        if self._pcontext:
            self._pcontext.close(death_sig)