import asyncio
from eventbus import EventBus
from orpa_agent import ORPAAgent
from ostp_agent import OSTPAgent

async def main():
    # Event bus başlat
    event_bus = EventBus()

    # OSTP + ORPA başlat
    ostp = OSTPAgent(event_bus, node_id="oscar-node-1", secret_key="supersecret")
    orpa = ORPAAgent(event_bus, node_id="oscar-node-1", secret_key="supersecret")

    # ORPA kendi handler’ını OSTP’ye kaydediyor
    await orpa.start()

    # ORPA üzerinden bir status mesajı gönder
    await orpa.report_project_status("project-123", "active")

if __name__ == "__main__":
    asyncio.run(main())
