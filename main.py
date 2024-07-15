import bcrypt
import psycopg2

conn = psycopg2.connect(
    database="n48",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()


def create_users_table1():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    ''')
    conn.commit()


create_users_table()


def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, hashed_password.decode('utf-8'))
    )
    conn.commit()

def check_password(username, password):
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    stored_hashed_password = cursor.fetchone()[0]

    if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
        return True
    else:
        return False


register_user('new_user', 'secure_password')
is_valid = check_password('new_user', 'secure_password')
print(is_valid)
