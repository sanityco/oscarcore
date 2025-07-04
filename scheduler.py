# scheduler.py
from task_scheduler import TaskScheduler

class Scheduler:
    def __init__(self):
        self.task_scheduler = TaskScheduler()

    def add_job(self, job_name, job_fn, priority=5):
        self.task_scheduler.add_task(job_name, job_fn, priority)

    async def run(self):
        await self.task_scheduler.run()
