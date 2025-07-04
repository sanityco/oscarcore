# oscar/core/plugin_manager.py

class PluginManager:
    """
    Oscar için plugin yönetici. Dinamik olarak plugin fonksiyonlarını yükler ve çalıştırır.
    """
    def __init__(self, config):
        self.config = config
        self.plugins = []

    def load_plugin(self, plugin_fn):
        """
        Tek bir plugin fonksiyonunu yükle ve çalıştır.
        """
        plugin_fn(self.config)
        self.plugins.append(plugin_fn)
        print(f"[PluginManager] Plugin yüklendi: {plugin_fn.__name__}")

    def load_plugins(self, plugin_list):
        """
        Birden fazla plugin fonksiyonunu liste halinde yükle.
        """
        for plugin_fn in plugin_list:
            self.load_plugin(plugin_fn)
