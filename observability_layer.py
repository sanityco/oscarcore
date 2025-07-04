import json
import os
import time

class ObservabilityLayer:
    def __init__(self, event_bus, log_file="logs/observability.log"):
        self.event_bus = event_bus
        self.log_file = log_file
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    async def on_event(self, event_str):
        self.log_event(event_str)

    def log_event(self, event_str):
        try:
            event = json.loads(event_str)
            log_entry = {
                "timestamp": time.time(),
                "trace_id": event.get("trace_id"),
                "node_id": event.get("node_id", "unknown"),
                "resource": event.get("event", {}).get("resource"),
                "status": event.get("status"),
                "latency_ms": event.get("latency_ms"),
                "decision": event.get("decision", "n/a"),
                "event": event
            }
            with open(self.log_file, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
            print(f"[Observability] Logged event {log_entry['trace_id']}")
        except Exception as e:
            print(f"[Observability] Failed to log event: {e}")

    def start(self):
        self.event_bus.subscribers.append(self)
        print("[Observability] Subscribed to event bus.")
