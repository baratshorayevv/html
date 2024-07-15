from passlib.context import CryptContext
from db import get_connection
from models import User, TodoItem

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def register_user(username: str, password: str) -> User:
    hashed_password = hash_password(password)
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, hashed_password) VALUES (%s, %s) RETURNING id, username, hashed_password",
        (username, hashed_password)
    )
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return User(id=user[0], username=user[1], hashed_password=user[2])
