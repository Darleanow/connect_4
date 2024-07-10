import asyncio
from websockets.sync.client import connect

def send_message():
        message = input(">")
        websocket.send(message)

with connect("ws://localhost:8000") as websocket:
    while True:
        send_message()