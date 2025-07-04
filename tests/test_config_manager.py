from config_manager import ConfigManager

def main():
    cm = ConfigManager()
    print(f"App Name: {cm.get('app_name')}")
    cm.set("new_param", "test_value")
    print(f"New Param: {cm.get('new_param')}")
    cm.save()
    cm.reload_config()
    print(f"After reload, App Name: {cm.get('app_name')}")

if __name__ == "__main__":
    main()
