import asyncio
import sys
from distributed_coordinator import DistributedCoordinator

async def main():
    node_id = sys.argv[1] if len(sys.argv) > 1 else "default-node"
    coordinator = DistributedCoordinator(node_id=node_id, all_nodes=["node-1", "node-2", "node-3"])
    await coordinator.elect_leader()

if __name__ == "__main__":
    asyncio.run(main())
