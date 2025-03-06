from fastapi import WebSocket
import random
import asyncio

websocket_clients = []

async def websocket_data(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.append(websocket)
    try:
        while True:
            data = {"time": random.randint(1, 100), "value": random.randint(1, 100)}
            for client in websocket_clients:
                await client.send_json(data)
            await asyncio.sleep(1)  # Send data every second
    except Exception:
        websocket_clients.remove(websocket)