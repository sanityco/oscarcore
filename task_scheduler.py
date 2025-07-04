import asyncio
import heapq

class TaskScheduler:
    def __init__(self):
        self.queue = []

    def add_task(self, task_name, task_fn, priority=5):
        heapq.heappush(self.queue, (priority, task_name, task_fn))
        print(f"[Scheduler] Task added: {task_name} (priority: {priority})")

    async def run(self):
        while self.queue:
            priority, task_name, task_fn = heapq.heappop(self.queue)
            print(f"[Scheduler] Running task: {task_name}")
            await task_fn()
            print(f"[Scheduler] Task {task_name} completed.")
