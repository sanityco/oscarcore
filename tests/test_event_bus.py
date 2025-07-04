import sys
import os
import asyncio

# core klasörünü modül yoluna ekle
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "core"))

from event_bus import EventBus

async def sample_callback(event):
    print(f"[Callback] Event alındı: {event}")

async def main():
    print("[Test] EventBus testi başlıyor…")
    bus = EventBus()
    bus.subscribe(sample_callback)
    # Dikkat: publish fonksiyonuna dict ver!
    await bus.publish({"type": "test_event", "payload": {"foo": "bar"}})
    # Eventin işlenmesi için ufak bir gecikme
    await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())
