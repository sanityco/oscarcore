import time

class MessageRouter:
    """
    Oscar'ın merkezi mesaj yönlendiricisi.
    Her agent/plugin bu router'a abone olabilir ve kendine gelen mesajları alır.
    """
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, name, handler):
        """
        Bir agent/plugin kendine gelen mesajları almak için kaydolur.
        """
        self.subscribers[name] = handler

    def unsubscribe(self, name):
        """
        Aboneliği kaldırır.
        """
        if name in self.subscribers:
            del self.subscribers[name]

    def route_message(self, to, msg):
        """
        Mesajı ilgili aboneye iletir.
        """
        if to in self.subscribers:
            self.subscribers[to](msg)
            print(f"[Router] Mesaj '{to}' agentına iletildi: {msg}")
        else:
            print(f"[Router] Hedef '{to}' bulunamadı, mesaj teslim edilemedi.")

    def broadcast(self, msg):
        """
        Tüm abonelere mesaj yollar.
        """
        for name, handler in self.subscribers.items():
            handler(msg)
        print(f"[Router] Broadcast: {msg} ({len(self.subscribers)} agent/plugin)")
