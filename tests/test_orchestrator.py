import sys
import os
import asyncio

sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

from event_bus import EventBus
from orchestrator import Orchestrator

print("[Test] Orchestrator MVP+++ testi başlıyor…")

async def async_module(event):
    print(f"[AsyncModül] Event alındı: {event}")

def sync_module(event):
    print(f"[SyncModül] Event alındı: {event}")

async def main():
    bus = EventBus()
    orchestrator = Orchestrator(bus)
    orchestrator.register_module("async_modül", async_module, event_type="greeting")
    orchestrator.register_module("sync_modül", sync_module)  # Tüm eventleri alır

    print("[Test] Kayıtlı modüller:", orchestrator.list_modules())

    # Event tipli gönder
    await bus.publish({"type": "greeting", "payload": {"msg": "Selam Oscar!"}})
    await bus.publish({"type": "ping", "payload": {"msg": "Ping Oscar"}})

    await asyncio.sleep(0.2)  # Callbacklerin işlenmesi için kısa bekleme

if __name__ == "__main__":
    asyncio.run(main())
