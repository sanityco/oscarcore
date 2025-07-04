import threading

class ResourceManager:
    def __init__(self, total_resources: int):
        self.total_resources = total_resources
        self.available_resources = total_resources
        self.lock = threading.Lock()

    def allocate(self, amount: int) -> bool:
        with self.lock:
            if self.available_resources >= amount:
                self.available_resources -= amount
                print(f"[ResourceManager] Allocated {amount} units. Remaining: {self.available_resources}")
                return True
            else:
                print(f"[ResourceManager] Allocation failed. Requested: {amount}, Available: {self.available_resources}")
                return False

    def release(self, amount: int):
        with self.lock:
            self.available_resources += amount
            if self.available_resources > self.total_resources:
                self.available_resources = self.total_resources
            print(f"[ResourceManager] Released {amount} units. Available: {self.available_resources}")

    def status(self) -> dict:
        return {
            "total": self.total_resources,
            "available": self.available_resources,
            "used": self.total_resources - self.available_resources
        }
