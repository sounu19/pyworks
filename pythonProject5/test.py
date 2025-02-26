import secrets
import time
from hashlib import sha256
import mysql.connector

# MySQL database connection details
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Replace with your MySQL root password
    'database': 'session_db'  # Replace with your database name
}

SESSION_TIMEOUT = 10 * 60  # 10 minutes in seconds


def connect_db():
    """Connect to the MySQL database"""
    return mysql.connector.connect(**DB_CONFIG)


def setup_database():
    """Ensure the necessary table exists"""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            username VARCHAR(255) PRIMARY KEY,
            session_token VARCHAR(255),
            password_hash VARCHAR(255),
            created_at BIGINT
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()


def hash_password(password):
    """Hash the password for secure storage"""
    return sha256(password.encode()).hexdigest()


def create_session(username, password):
    """Create a new session for the user and store it in the database"""
    password_hash = hash_password(password)
    session_token = secrets.token_hex(16)
    created_at = int(time.time())

    conn = connect_db()
    cursor = conn.cursor()

    # Insert or update session details
    cursor.execute('''
        INSERT INTO sessions (username, session_token, password_hash, created_at)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        session_token = VALUES(session_token),
        password_hash = VALUES(password_hash),
        created_at = VALUES(created_at)
    ''', (username, session_token, password_hash, created_at))

    conn.commit()
    cursor.close()
    conn.close()

    return session_token


def is_session_valid(username):
    """Check if the session for the user is still valid"""
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM sessions WHERE username = %s', (username,))
    session = cursor.fetchone()
    cursor.close()
    conn.close()

    if not session:
        return False

    current_time = int(time.time())
    if current_time - session['created_at'] > SESSION_TIMEOUT:
        delete_session(username)
        return False

    return True


def get_session(username):
    """Retrieve the session token if valid"""
    if is_session_valid(username):
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT session_token FROM sessions WHERE username = %s', (username,))
        session = cursor.fetchone()

        cursor.close()
        conn.close()

        if session:
            return session['session_token']

    return None


def delete_session(username):
    """Delete a user's session from the database"""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM sessions WHERE username = %s', (username,))

    conn.commit()
    cursor.close()
    conn.close()


# Example usage
def main():
    setup_database()
    print("Welcome!\n")

    while True:
        print("1. Create session")
        print("2. Check session")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")

            session_token = create_session(username, password)
            print(f"Session created! Token: {session_token}\n")

        elif choice == '2':
            username = input("Enter username: ")

            if is_session_valid(username):
                token = get_session(username)
                print(f"Session is valid! Token: {token}\n")
            else:
                print("Session has expired or does not exist.\n")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
