# job_orchestrator.py

from resource_manager import ResourceManager
from scheduler import Scheduler
import asyncio

class JobOrchestrator:
    def __init__(self, event_bus, resource_manager: ResourceManager, scheduler: Scheduler):
        self.event_bus = event_bus
        self.resource_manager = resource_manager
        self.scheduler = scheduler

    async def submit_job(self, job_name, required_units=1, priority=5, payload=None):
        if self.resource_manager.allocate(required_units):
            self.scheduler.add_task(job_name, priority, self.execute_job, payload or {}, required_units)
        else:
            print(f"[Orchestrator] Not enough resources for job: {job_name}")

    async def execute_job(self, payload, required_units):
        job_name = payload.get("job_name", "UnnamedJob")
        print(f"[Orchestrator] Executing job: {job_name}")
        await asyncio.sleep(1)  # Simulate job
        print(f"[Orchestrator] Job completed: {job_name}")
        self.resource_manager.release(required_units)

    def status(self):
        return {
            "resources": self.resource_manager.status()
        }
