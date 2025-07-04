import asyncio
from core import Core
from ostp_agent import OSTPAgent
from observability_layer import ObservabilityLayer

async def main():
    core = Core()
    ostp = OSTPAgent(core.event_bus, node_id="oscar-node-1", secret_key="supersecret")
    observability = ObservabilityLayer(core.event_bus)

    await ostp.load_plugins()
    observability.start()

    test_payload = {
        "type": "query",
        "resource": "/healthcheck",
        "data": {}
    }

    for _ in range(3):
        await ostp.send_message("oscar-node-1", test_payload)
        await asyncio.sleep(0.5)

    print("[Test] Completed. Check logs/observability.log for output.")

if __name__ == "__main__":
    asyncio.run(main())
