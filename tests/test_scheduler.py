import asyncio
from task_scheduler import TaskScheduler, Task

async def main():
    scheduler = TaskScheduler()
    await scheduler.start()

    await scheduler.add_task(Task("low-priority-task", priority=5))
    await scheduler.add_task(Task("high-priority-task", priority=1))
    await scheduler.add_task(Task("medium-priority-task", priority=3))

    await asyncio.sleep(5)  # işleri bitirmesi için zaman ver

    await scheduler.stop()

if __name__ == "__main__":
    asyncio.run(main())
