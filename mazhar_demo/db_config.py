import mysql.connector

# Database configuration
DB_CONFIG = {
    'host': '10.22.200.123',
    'database': 'mazhar_testing',
    'user': 'mazhar',
    'password': 'mazhar@123'
}

def get_db_mysql_connection():
    """
    Establish a connection to the MySQL database and return the connection object.
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        raise Exception(f"Database connection error: {err}")
