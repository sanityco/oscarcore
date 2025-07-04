# sentinel.py

import time

class Sentinel:
    """
    Basit rate-limiting ve yetkilendirme mekanizması.
    """
    def __init__(self):
        # Node bazlı izin durumu ve istek zamanlarını takip eden sözlük.
        self.node_access = {}
        self.rate_limit_window = 5  # saniye
        self.max_requests_per_window = 10

    def authorize(self, node_id):
        """
        Bir node’un yetkisini ve rate-limit durumunu kontrol eder.
        """
        now = time.time()
        record = self.node_access.get(node_id, {"timestamps": [], "blocked": False})

        if record["blocked"]:
            return "blocked"

        # Eski istekleri temizle
        record["timestamps"] = [
            ts for ts in record["timestamps"] if now - ts < self.rate_limit_window
        ]

        # Yeni istek kaydı
        record["timestamps"].append(now)

        if len(record["timestamps"]) > self.max_requests_per_window:
            record["blocked"] = True
            self.node_access[node_id] = record
            print(f"[Sentinel] Node blocked: {node_id}")
            return "rate_limited"

        self.node_access[node_id] = record
        return "authorized"

    def reset(self, node_id):
        """
        Bir node’un engelini kaldırır.
        """
        if node_id in self.node_access:
            self.node_access[node_id] = {"timestamps": [], "blocked": False}
            print(f"[Sentinel] Node reset: {node_id}")
