import json
import time

class Sentinel:
    def __init__(self):
        self.allowed_nodes = set()
        self.blocked_nodes = {}
        self.request_log = {}
        self.rate_limit_threshold = 10
        self.rate_limit_window = 5.0  # saniye
        self.block_duration = 30.0   # saniye

    def allow_node(self, node_id):
        self.allowed_nodes.add(node_id)
        self.blocked_nodes.pop(node_id, None)
        print(f"[Sentinel] Node allowed: {node_id}")

    def block_node(self, node_id):
        self.blocked_nodes[node_id] = time.time() + self.block_duration
        self.allowed_nodes.discard(node_id)
        print(f"[Sentinel] Node blocked: {node_id}")

    def unblock_expired_nodes(self):
        now = time.time()
        expired = [node for node, until in self.blocked_nodes.items() if now >= until]
        for node in expired:
            print(f"[Sentinel] Node automatically unblocked: {node}")
            del self.blocked_nodes[node]

    def authorize(self, event):
        self.unblock_expired_nodes()
        node_id = event.get("from")
        trace_id = event.get("trace_id", "unknown")

        if node_id in self.blocked_nodes:
            self.log_decision(node_id, trace_id, "blocked")
            return False

        if self.allowed_nodes and node_id not in self.allowed_nodes:
            self.log_decision(node_id, trace_id, "not_whitelisted")
            return False

        if not self.check_rate_limit(node_id):
            self.block_node(node_id)
            self.log_decision(node_id, trace_id, "rate_limited")
            return False

        self.log_decision(node_id, trace_id, "authorized")
        return True

    def check_rate_limit(self, node_id):
        now = time.time()
        log = self.request_log.setdefault(node_id, [])
        log.append(now)
        log[:] = [ts for ts in log if now - ts <= self.rate_limit_window]
        return len(log) <= self.rate_limit_threshold

    def log_decision(self, node_id, trace_id, decision):
        log = {
            "timestamp": time.time(),
            "trace_id": trace_id,
            "node_id": node_id,
            "decision": decision
        }
        print(json.dumps(log, indent=2))