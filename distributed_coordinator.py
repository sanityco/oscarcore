import asyncio
import random

class DistributedCoordinator:
    def __init__(self, node_id, all_nodes):
        self.node_id = node_id
        self.all_nodes = all_nodes
        self.leader = None

    async def elect_leader(self):
        self.leader = min(self.all_nodes)  # basitçe id’ye göre
        print(f"[Coordinator] New leader elected: {self.leader}")
        await self.heartbeat()

    async def heartbeat(self):
        for _ in range(5):  # sadece 5 tur döndür
            await asyncio.sleep(1)
            for node in self.all_nodes:
                if node == self.node_id:
                    continue
                alive = random.choice([True, False])
                if alive:
                    print(f"[Coordinator] Node {node} is UP.")
                else:
                    print(f"[Coordinator] Node {node} is DOWN.")
