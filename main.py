from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from typing import List, Dict
from database import messages_collection
from models import MessageModel
from datetime import datetime

app = FastAPI()

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections[websocket] = username
        await self.broadcast(f"🔵 {username} joined the chat!")

    def disconnect(self, websocket: WebSocket):
        username = self.active_connections.pop(websocket, "Unknown")
        return username

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
def read_root():
    return {"message": "FastAPI Chat App Running!"}

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    """Handle WebSocket connections and save messages to MongoDB"""
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            
            # Save message to MongoDB
            new_message = MessageModel(username=username, content=data)
            await messages_collection.insert_one(new_message.dict())

            await manager.broadcast(f"💬 {username}: {data}")
    except WebSocketDisconnect:
        left_user = manager.disconnect(websocket)
        await manager.broadcast(f"🔴 {left_user} left the chat!")

@app.get("/messages")
async def get_messages():
    """Fetch last 20 messages from MongoDB"""
    messages = await messages_collection.find().sort("timestamp", -1).limit(20).to_list(None)
    return [
        {"username": msg["username"], "content": msg["content"], "timestamp": msg["timestamp"]}
        for msg in messages
    ]
