import asyncio

class EventBus:
    def __init__(self):
        self.subscribers = []

    def register(self, subscriber):
        self.subscribers.append(subscriber)

    async def publish(self, event):
        for subscriber in self.subscribers:
            await subscriber.on_event(event)