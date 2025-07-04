import yaml
import os

class ConfigManager:
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        self.config = {}
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file {self.config_path} not found.")
        with open(self.config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        print(f"[ConfigManager] Config loaded from {self.config_path}")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def reload_config(self):
        self.load_config()
        print("[ConfigManager] Config reloaded.")

    def save(self):
        with open(self.config_path, 'w') as f:
            yaml.dump(self.config, f)
        print("[ConfigManager] Config saved to disk.")
