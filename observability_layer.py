import time
import json
import os

class ObservabilityLayer:
    def __init__(self, event_bus, log_file="logs/observability.log"):
        self.event_bus = event_bus
        self.log_file = log_file

        # Log dizini yoksa oluştur
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    async def start(self):
        """
        Event bus’a abone olur ve loglamayı başlatır.
        """
        self.event_bus.subscribe(self._log_event)
        print("[Observability] Subscribed to event bus.")

    async def _log_event(self, event):
        """
        Gelen her mesajı log dosyasına yazar.
        """
        try:
            message = json.loads(event)
            log_entry = {
                "timestamp": time.time(),
                "event": message
            }
            with open(self.log_file, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
            print(f"[Observability] Logged event {message.get('trace_id')}")
        except Exception as e:
            print(f"[Observability] Error logging event: {e}")
