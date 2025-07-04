import asyncio
import json
import uuid
import time
from discovery import Discovery
from sentinel import Sentinel

class OSTPAgent:
    def __init__(self, event_bus, node_id, secret_key):
        self.event_bus = event_bus
        self.node_id = node_id
        self.secret_key = secret_key
        self.discovery = Discovery(node_id)
        self.sentinel = Sentinel()
        self.handlers = {}

    async def load_plugins(self, plugins_dir="plugins"):
        import os
        import importlib.util

        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py"):
                path = os.path.join(plugins_dir, filename)
                spec = importlib.util.spec_from_file_location(filename[:-3], path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, "register"):
                    mod.register(self)
                    print(f"[OSTP] Plugin loaded: {filename}")

    def register_handler(self, resource, handler):
        self.handlers[resource] = handler
        print(f"[OSTP] Registered handler for {resource}")

    async def handle_request(self, message):
        event = json.loads(message)
        trace_id = event.get("trace_id", str(uuid.uuid4()))
        node_id = event.get("from", "unknown")
        resource = event.get("payload", {}).get("resource", "/unknown")

        decision = self.sentinel.authorize(node_id)
        response = {
            "timestamp": time.time(),
            "trace_id": trace_id,
            "node_id": node_id,
            "decision": decision
        }
        print(json.dumps(response, indent=2))

        if decision != "authorized":
            response.update({
                "status": "unauthorized",
                "latency_ms": 1.0,
                "event": event
            })
            await self._send(node_id, response)
            return

        handler = self.handlers.get(resource)
        if handler:
            result = await handler(event)
            response.update({
                "trace_id": trace_id,
                "timestamp": time.time(),
                "status": "query_success",
                "latency_ms": 0.5,
                "event": result
            })
            print(json.dumps(response, indent=2))
            await self._send(node_id, response)

    async def _send(self, to_node, payload):
        message = {
            "timestamp": time.time(),
            "trace_id": str(uuid.uuid4()),
            "from": self.node_id,
            "to": to_node,
            "schema_version": "1.0",
            "payload": payload,
            "signature": uuid.uuid4().hex
        }
        await self.event_bus.publish(json.dumps(message))
        print(f"[OSTP] Sent message: {message['trace_id']} to {to_node}")

    async def send_message(self, to_node, payload):
        await self._send(to_node, payload)
