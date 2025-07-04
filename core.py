import asyncio
from eventbus import EventBus

class Core:
    def __init__(self):
        self.event_bus = EventBus()
        self.agents = []

    def register_agent(self, agent):
        self.agents.append(agent)
        self.event_bus.register(agent)

    async def run(self, duration=3):
        print("[Core] Starting event loop…")
        await asyncio.sleep(duration)
        print("[Core] Event loop stopped.")