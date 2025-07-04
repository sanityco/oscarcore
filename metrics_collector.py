import time
import psutil

class MetricsCollector:
    def __init__(self):
        self.metrics = {}

    def collect(self):
        self.metrics["timestamp"] = time.time()
        self.metrics["cpu_percent"] = psutil.cpu_percent(interval=1)
        self.metrics["memory_percent"] = psutil.virtual_memory().percent
        self.metrics["disk_usage_percent"] = psutil.disk_usage('/').percent
        return self.metrics

    def print_metrics(self):
        print(f"[Metrics] CPU: {self.metrics['cpu_percent']}% | "
              f"Memory: {self.metrics['memory_percent']}% | "
              f"Disk: {self.metrics['disk_usage_percent']}%")
