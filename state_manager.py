import json
import os

class StateManager:
    def __init__(self, state_file="state.json"):
        self.state_file = state_file
        self.state = {}
        self._load_state()

    def _load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, "r") as f:
                self.state = json.load(f)
        else:
            self.state = {}

    def _save_state(self):
        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=2)

    def get_state(self, job_id):
        return self.state.get(job_id, None)

    def set_state(self, job_id, job_state):
        self.state[job_id] = job_state
        self._save_state()

    def delete_state(self, job_id):
        if job_id in self.state:
            del self.state[job_id]
            self._save_state()

    def all_states(self):
        return self.state
