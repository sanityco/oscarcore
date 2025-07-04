
def register(ostp_agent):
    async def hello_handler(data):
        return {"status": "ok", "message": "Hello from plugin!"}
    ostp_agent.register_handler("/hello", hello_handler)
