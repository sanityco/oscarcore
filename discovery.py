import json
import time

class Discovery:
    def __init__(self, node_id):
        self.node_id = node_id
        self.known_nodes = set()

    def process_discovery(self, event):
        sender = event.get("from")
        if sender and sender != self.node_id:
            self.known_nodes.add(sender)
            self.log_discovery(sender)

    def build_discovery_message(self):
        return {
            "type": "discovery",
            "resource": "/discovery",
            "data": {}
        }

    def log_discovery(self, sender):
        log = {
            "timestamp": time.time(),
            "discovered_node": sender,
            "known_nodes": list(self.known_nodes)
        }
        print(json.dumps(log, indent=2))