# test_job_orchestrator.py
import asyncio
from scheduler import Scheduler

async def job1():
    print("[JobOrchestrator] Job 1 executed")

async def job2():
    print("[JobOrchestrator] Job 2 executed")

async def main():
    scheduler = Scheduler()

    scheduler.add_job("job1", job1, priority=1)
    scheduler.add_job("job2", job2, priority=2)

    await scheduler.run()

if __name__ == "__main__":
    asyncio.run(main())
