from state_manager import StateManager

sm = StateManager()

sm.set_state("job1", {"status": "running"})
sm.set_state("job2", {"status": "completed"})

print("[Test] job1 state:", sm.get_state("job1"))
print("[Test] job2 state:", sm.get_state("job2"))

sm.delete_state("job1")

print("[Test] After delete job1:", sm.get_state("job1"))
print("[Test] All states:", sm.all_states())
