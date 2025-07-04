class NotificationManager:
    def __init__(self):
        self.channels = []

    def register_channel(self, channel):
        self.channels.append(channel)

    def send(self, message, level="info"):
        for channel in self.channels:
            channel.send(message, level)

# Örnek kanal sınıfı
class ConsoleChannel:
    def send(self, message, level):
        print(f"[{level.upper()}] {message}")
