from models import User
from db import get_connection

def get_user_by_username(username: str) -> User:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username, hashed_password FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        return User(id=user[0], username=user[1], hashed_password=user[2])
    return None
