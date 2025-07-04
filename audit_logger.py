import json
import time
from datetime import datetime

class AuditLogger:
    def __init__(self, log_file="audit.log"):
        self.log_file = log_file

    def log_event(self, user, action, resource, details=None):
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "user": user,
            "action": action,
            "resource": resource,
            "details": details or {},
        }
        with open(self.log_file, "a") as f:
            f.write(json.dumps(event) + "\n")
        print(f"[Audit] Logged event: {event}")
