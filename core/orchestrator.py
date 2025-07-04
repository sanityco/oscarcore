import asyncio

class Orchestrator:
    """
    Oscar çekirdeğinin gelişmiş orchestrator katmanı.
    Modülleri isimle kaydeder, event tipi filtreleme ve hata loglaması sağlar.
    """
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.modules = {}  # {'modül_ismi': {'callback': func, 'event_type': ...}}

    def register_module(self, module_name, callback, event_type=None):
        """
        Modülü isimle kaydet. event_type verilirse sadece o tür event’leri alır.
        """
        self.modules[module_name] = {'callback': callback, 'event_type': event_type}
        self.event_bus.subscribe(lambda event, cb=callback, et=event_type: self._dispatch(cb, et, event))
        print(f"[Orchestrator] Modül kaydedildi: {module_name} (event_type={event_type})")

    async def _dispatch(self, callback, event_type, event):
        try:
            # Event type filtrelemesi
            if event_type and event.get("type") != event_type:
                return
            if asyncio.iscoroutinefunction(callback):
                await callback(event)
            else:
                callback(event)
        except Exception as e:
            print(f"[Orchestrator] Modül '{callback.__name__}' event işlerken hata: {e}")

    def list_modules(self):
        return list(self.modules.keys())

    async def start(self):
        print("[Orchestrator] Başladı.")
        # Gerekirse orchestrator’a arka planda görev (monitor, health vs.) ekle.
        while True:
            await asyncio.sleep(2)  # Placeholder heartbeat

    def stop(self):
        print("[Orchestrator] Durduruldu.")
