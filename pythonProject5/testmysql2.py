import random
import string
import time
import mysql.connector
from datetime import datetime, timedelta

# Database connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",       # Change to your host
        user="root",            # Your MySQL username
        password="your_password",  # Your MySQL password
        database="your_database"   # Your database name
    )

# Create the sessions table (if not already exists)
def initialize_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            token VARCHAR(255) PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            expiration_time DATETIME NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

# Generate a random session token and store it in the database
def generate_session(username, password):
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    expiration_time = datetime.now() + timedelta(minutes=10)

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO sessions (token, username, expiration_time) VALUES (%s, %s, %s)",
        (token, username, expiration_time)
    )
    connection.commit()
    cursor.close()
    connection.close()

    print(f"Session created for user '{username}'. Token: {token}")
    return token

# Validate a session token by checking its expiration time
def validate_session(token):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT username, expiration_time FROM sessions WHERE token = %s", (token,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        username, expiration_time = result
        if datetime.now() < expiration_time:
            print(f"Session is valid for user: {username}")
            return True
        else:
            print(f"Session expired for token: {token}")
            delete_session(token)
    else:
        print(f"Invalid session token: {token}")
    return False

# Delete a session token from the database
def delete_session(token):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM sessions WHERE token = %s", (token,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Session deleted for token: {token}")

# Periodically clean up expired sessions from the database
def cleanup_expired_sessions():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM sessions WHERE expiration_time < NOW()")
    connection.commit()
    cursor.close()
    connection.close()
    print("Expired sessions cleaned up")

# Main script
if __name__ == "__main__":
    # Initialize database table
    initialize_table()

    # Get user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Generate a session token
    session_token = generate_session(username, password)

    # Simulate session validation
    time.sleep(5)  # Wait 5 seconds
    validate_session(session_token)  # Validate session

    # Simulate after session expiration
    time.sleep(605)  # Wait for 10 minutes + extra seconds
    validate_session(session_token)  # Validate session again
