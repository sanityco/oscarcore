import yaml

class ConfigurationValidator:
    def __init__(self, schema: dict):
        self.schema = schema

    def validate(self, config_path: str) -> bool:
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)

            for key, value_type in self.schema.items():
                if key not in config:
                    print(f"[ConfigValidator] Missing key: {key}")
                    return False
                if not isinstance(config[key], value_type):
                    print(f"[ConfigValidator] Invalid type for key: {key}, expected {value_type}")
                    return False

            print(f"[ConfigValidator] Configuration is valid.")
            return True

        except Exception as e:
            print(f"[ConfigValidator] Validation error: {e}")
            return False
