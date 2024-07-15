from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    username: str
    hashed_password: str

class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    user_id: int
