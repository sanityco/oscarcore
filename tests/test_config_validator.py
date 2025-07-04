from config_validator import ConfigurationValidator

def main():
    schema = {
        "app_name": str,
        "version": str,
        "max_workers": int
    }

    validator = ConfigurationValidator(schema)

    result = validator.validate("config.yaml")
    print(f"[Test] Validation result: {result}")

if __name__ == "__main__":
    main()
