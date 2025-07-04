import asyncio
import uuid

class EventBus:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    async def publish(self, event: dict):
        if not isinstance(event, dict):
            raise ValueError("Event must be a dictionary")
        event.setdefault("trace_id", str(uuid.uuid4()))
        for subscriber in self.subscribers:
            # subscriber async mi sync mi otomatik ayıkla:
            if asyncio.iscoroutinefunction(subscriber):
                asyncio.create_task(subscriber(event))
            else:
                # Eğer subscriber bir lambda ise, içte async çağırıyorsa: 
                # Kapsayıcıda await desteklemeli!
                result = subscriber(event)
                if asyncio.iscoroutine(result):
                    asyncio.create_task(result)
