from ostp_agent import OSTPAgent
import json
import time
import uuid

class ORPAAgent(OSTPAgent):
    def __init__(self, event_bus, node_id, secret_key):
        super().__init__(event_bus, node_id, secret_key)
        self.register_handler("/orpa/status", self.handle_status_request)

    async def handle_status_request(self, event):
        # basit örnek cevap
        return {
            "status": "ok",
            "timestamp": time.time(),
            "project_id": event.get("payload", {}).get("project_id", "unknown"),
            "state": event.get("payload", {}).get("state", "unknown")
        }

    async def report_project_status(self, project_id, state):
        payload = {
            "type": "status_report",
            "project_id": project_id,
            "state": state
        }
        await self.send_message(
            to_node=self.node_id,
            payload=payload
        )
