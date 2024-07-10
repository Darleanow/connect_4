import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print(f"Received: {message}")

async def main():
    async with serve(echo, "localhost", 8001):
        await asyncio.Future()

asyncio.run(main())