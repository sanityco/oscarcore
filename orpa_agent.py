from ostp_agent import OSTPAgent
import time
import uuid
import json

class ORPAAgent(OSTPAgent):
    def __init__(self, event_bus, node_id, secret_key):
        super().__init__(event_bus, node_id, secret_key)
        self.register_handler("/orpa/status", self._handle_status)

    async def report_project_status(self, project_id: str, status: str):
        """
        Proje durumunu Oscar’a rapor eder.
        """
        payload = {
            "type": "status_report",
            "resource": "/orpa/status",
            "data": {
                "project_id": project_id,
                "status": status,
                "timestamp": time.time()
            }
        }
        await self.send_message(self.node_id, payload)

    async def _handle_status(self, event):
        """
        Gelen durum güncellemelerini işler.
        """
        data = event.get("payload", {}).get("data", {})
        project_id = data.get("project_id", "unknown")
        status = data.get("status", "unknown")

        log_entry = {
            "trace_id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "project_id": project_id,
            "status": status
        }

        print(f"[ORPA] Project {project_id} status updated: {status}")
        return log_entry
