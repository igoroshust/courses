import asyncio


async def background_log():
    while True:
        print("heartbeat")
        await asyncio.sleep(1)


async def main():
    task = asyncio.create_task(background_log())
    
    await asyncio.sleep(3)
    
    task.cancel()
    
    
asyncio.run(
    main()
)