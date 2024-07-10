import asyncio
import websockets
from websockets.server import serve

async def handler(websocket):
    try:
        async for message in websocket:
            print(message)
    except websockets.ConnectionClosedOK:
        print("Connection closed normally")
    except websockets.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
    finally:
        print("Connection handler exited")

async def main():
    async with serve(handler, "localhost", 8001):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user")
