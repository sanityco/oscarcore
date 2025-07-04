# test_plugin_manager.py

from core.core import Config
from core.plugin_manager import PluginManager

def dummy_plugin(core):
    print("[DummyPlugin] Plugin çalıştı.")
    # Config örneğini kullanabilirsin, örn:
    core.set("dummy_key", "dummy_value")
    print("[DummyPlugin] Config güncellendi.")

def main():
    print("[Test] Plugin Manager test başlıyor…")
    config = Config("config.yaml")
    plugin_manager = PluginManager(config)

    # Tekli yükleme:
    plugin_manager.load_plugin(dummy_plugin)

    # Yükleme başarılıysa kontrol:
    value = config.get("dummy_key")
    print("[Test] Plugin effect:", value)

if __name__ == "__main__":
    main()
