import threading
import time

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self._running = False
        self.last_heartbeat = None

    def start(self):
        self._running = True
        self.last_heartbeat = time.time()
        print(f"[{self.name}] started.")

    def stop(self):
        self._running = False
        print(f"[{self.name}] stopped.")

    def is_alive(self):
        return self._running

    def heartbeat(self):
        self.last_heartbeat = time.time()

class AgentManager:
    def __init__(self):
        self.agents = {}
        self.lock = threading.Lock()

    def register(self, agent: BaseAgent):
        with self.lock:
            self.agents[agent.name] = agent
            print(f"[AgentManager] Agent registered: {agent.name}")

    def unregister(self, name):
        with self.lock:
            if name in self.agents:
                del self.agents[name]
                print(f"[AgentManager] Agent removed: {name}")

    def get(self, name):
        return self.agents.get(name)

    def list_agents(self):
        return list(self.agents.keys())

    def start_agent(self, name):
        agent = self.get(name)
        if agent and not agent.is_alive():
            agent.start()

    def stop_agent(self, name):
        agent = self.get(name)
        if agent and agent.is_alive():
            agent.stop()

    def health_check(self, threshold=10):
        now = time.time()
        report = {}
        for name, agent in self.agents.items():
            alive = agent.is_alive()
            last = agent.last_heartbeat or 0
            healthy = alive and (now - last < threshold)
            report[name] = {"alive": alive, "healthy": healthy, "last_heartbeat": last}
        return report

    def broadcast(self, msg):
        for agent in self.agents.values():
            if hasattr(agent, "on_message"):
                agent.on_message(msg)
