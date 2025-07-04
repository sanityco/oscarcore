import asyncio
from eventbus import EventBus
from orpa_agent import ORPAAgent

async def main():
    # EventBus ve ORPAAgent başlat
    event_bus = EventBus()
    orpa = ORPAAgent(event_bus, node_id="oscar-node-1", secret_key="supersecret")

    # Proje durumu raporla
    await orpa.report_project_status("project-123", "active")

if __name__ == "__main__":
    asyncio.run(main())
