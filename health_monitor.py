import psutil
import time

class HealthMonitor:
    def __init__(self, threshold_cpu=80.0, threshold_mem=80.0):
        self.threshold_cpu = threshold_cpu
        self.threshold_mem = threshold_mem

    def check_health(self):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        status = "healthy"

        if cpu > self.threshold_cpu or mem > self.threshold_mem:
            status = "unhealthy"

        return {
            "timestamp": time.time(),
            "cpu_percent": cpu,
            "mem_percent": mem,
            "status": status
        }
