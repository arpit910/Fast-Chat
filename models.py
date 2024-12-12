from pydantic import BaseModel
from datetime import datetime

class MessageModel(BaseModel):
    username: str
    content: str
    timestamp: datetime = datetime.utcnow()
 