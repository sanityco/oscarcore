from notification_manager import NotificationManager, ConsoleChannel

notif_mgr = NotificationManager()
console = ConsoleChannel()
notif_mgr.register_channel(console)

notif_mgr.send("System initialized.", level="info")
notif_mgr.send("High memory usage detected!", level="warning")
notif_mgr.send("Service crashed!", level="error")
