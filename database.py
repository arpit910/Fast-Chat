from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "chat_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Collections
messages_collection = db["messages"]
 