from agent_manager import AgentManager, BaseAgent
import time

class MyAgent(BaseAgent):
    def on_message(self, msg):
        print(f"[{self.name}] Got msg: {msg}")

def main():
    mgr = AgentManager()
    a1 = MyAgent("agent1")
    a2 = MyAgent("agent2")
    mgr.register(a1)
    mgr.register(a2)
    mgr.start_agent("agent1")
    mgr.start_agent("agent2")
    a1.heartbeat(); a2.heartbeat()
    print("[Test] Health:", mgr.health_check(threshold=5))
    mgr.broadcast("selam agents")
    time.sleep(6)
    print("[Test] Health (after 6s):", mgr.health_check(threshold=5))
    mgr.stop_agent("agent1")
    print("[Test] Agent list:", mgr.list_agents())
    mgr.unregister("agent2")
    print("[Test] Agent list (after remove):", mgr.list_agents())

if __name__ == "__main__":
    main()
