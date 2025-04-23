from typing import List
from fastapi import WebSocket

class WSManager:
    def __init__(self) -> None:
        self.active: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        if ws in self.active:
            self.active.remove(ws)

    async def broadcast(self, msg: dict):
        to_remove = []
        for ws in self.active:
            try:
                await ws.send_json(msg)
            except Exception:        # client dropped
                to_remove.append(ws)
        for ws in to_remove:
            self.disconnect(ws)


ws_manager = WSManager()
