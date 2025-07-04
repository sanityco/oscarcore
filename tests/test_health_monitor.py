from health_monitor import HealthMonitor
import time

monitor = HealthMonitor(threshold_cpu=80.0, threshold_mem=80.0)

print("[Test] Checking system health…")
result = monitor.check_health()
print(f"[Test] CPU: {result['cpu_percent']}% | MEM: {result['mem_percent']}% | Status: {result['status']}")
