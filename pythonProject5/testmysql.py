import mysql.connector

# Database connection details
host = "localhost"  # Change to your database host, e.g., 127.0.0.1
user = "your_username"  # Your MySQL username
password = "your_password"  # Your MySQL password
database = "your_database"  # Your database name

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Check if the connection is successful
    if connection.is_connected():
        print("Connected to MySQL database")

    # Create a cursor object
    cursor = connection.cursor()

    # Example query
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    print("Connected to database:", result[0])

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
