from message_router import MessageRouter

def agent1_handler(msg):
    print(f"[agent1] Gelen mesaj: {msg}")

def agent2_handler(msg):
    print(f"[agent2] Gelen mesaj: {msg}")

def main():
    router = MessageRouter()
    router.subscribe("agent1", agent1_handler)
    router.subscribe("agent2", agent2_handler)

    # Bireysel mesaj
    router.route_message("agent1", "Oscar’a selamlar!")
    router.route_message("agent2", "Agent2 burada mı?")
    router.route_message("bilinmeyen", "Bunu kimse almaz...")

    # Broadcast (tüm agent/plugin’lara aynı anda)
    router.broadcast("Herkese Oscar’dan sevgiler!")

if __name__ == "__main__":
    main()
