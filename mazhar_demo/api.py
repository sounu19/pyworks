from flask import Flask, request, jsonify
import random
import time
from db_config import get_db_mysql_connection

app = Flask(__name__)

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')



    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    try:
        conn = get_db_mysql_connection()
        cursor = conn.cursor(dictionary=True)

        # Check if username exists
        cursor.execute("SELECT * FROM login_details WHERE username = %s", (username,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "No Username found"}), 404

        # Check session_token
        if user['session_token'] is not '0':
            return jsonify({"message": "User is already logged in"}), 403

        # Check password
        if user['password'] != password:
            return jsonify({"message": "Password did not match"}), 403

        # Generate session token and store it
        session_token = str(random.randint(100000, 999999))
        session_time = int(time.time())  # Current Unix time
        cursor.execute(
            "UPDATE login_details SET session_token = %s, session_time = %s WHERE id = %s",
            (session_token, session_time, user['id'])
        )
        conn.commit()

        return jsonify({"message": "User login successful", "session_token": session_token}), 200
    except Exception as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()


# Retrieve data endpoint
@app.route('/retrieve', methods=['POST'])
def retrieve_data():
    data = request.json
    session_token = data.get('session_token')
    vehicle_id = data.get('vehicle_id')

    if not session_token or not vehicle_id:
        return jsonify({"message": "Session token and vehicle ID are required"}), 400

    try:
        conn = get_db_mysql_connection()
        cursor = conn.cursor(dictionary=True)

        # Check session token
        cursor.execute("SELECT * FROM login_details WHERE session_token = %s", (session_token,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "You are not logged in. Please login first"}), 403

        # Retrieve vehicle details
        cursor.execute("SELECT * FROM vehicle_details WHERE vehicle_id = %s", (vehicle_id,))
        vehicle = cursor.fetchone()

        if not vehicle:
            return jsonify({"message": "No vehicle found with the given ID"}), 404

        return jsonify({"message": "Vehicle data retrieved successfully", "data": vehicle}), 200
    except Exception as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='10.22.202.219', port=5100, debug=True)
