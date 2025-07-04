import yaml

class Core:
    """
    Oscar’ın ana çekirdeği — tüm sistem modüllerinin birleştiği yapı.
    """
    def __init__(self, config_path="config.yaml"):
        self.config = Config(config_path)
        self.state = "init"

class Config:
    """
    Oscar’ın merkezi yapılandırma yükleyicisi ve yöneticisi.
    """

    def __init__(self, path="config.yaml"):
        self.path = path
        self.data = {}
        self.load()

    def load(self):
        """
        Diskten config yükle.
        """
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = yaml.safe_load(f) or {}
            print(f"[Config] Config yüklendi: {self.path}")
        except FileNotFoundError:
            print(f"[Config] {self.path} bulunamadı, varsayılan başlatıldı.")
            self.data = {}

    def save(self):
        """
        Diske config kaydet.
        """
        with open(self.path, "w", encoding="utf-8") as f:
            yaml.safe_dump(self.data, f)
        print(f"[Config] Config diske kaydedildi: {self.path}")

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save()
