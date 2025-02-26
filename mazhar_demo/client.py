import requests
import json

# API Endpoints
LOGIN_URL = "http://10.22.202.219:5100/login"
RETRIEVE_URL = "http://10.22.202.219:5100/retrieve"

# Session token storage (only for the runtime)
session_token = None


def login():
    """Perform the login process and return the session token."""
    global session_token
    print("\n--- Login Required ---")
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        try:
            response = requests.post(LOGIN_URL, json={"username": username, "password": password})

            # Check if the response status code is 200
            if response.status_code == 200:
                data = response.json()
                print("Login successful!")
                session_token = data["session_token"]
                return session_token

            # Handle invalid login credentials
            if response.status_code == 401:
                print("Error: Invalid username or password.")
            else:
                print(f"Error: {response.text.strip()}")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        except json.JSONDecodeError:
            print("Error: Received an invalid response from the server.")

        retry = input("Do you want to try logging in again? (yes/no): ").strip().lower()
        if retry != "yes":
            return None



def retrieve_vehicle_data(vehicle_id):
    """Retrieve vehicle data from the API."""
    global session_token
    response = requests.post(RETRIEVE_URL, json={"session_token": session_token, "vehicle_id": vehicle_id})
    return response


def main():
    """Main CLI client logic."""
    global session_token
    print("\n--- CLI Client ---")
    while True:
        # Ensure the user is logged in
        if not session_token:
            print("You are not logged in. Please log in to continue.")
            session_token = login()
            if not session_token:
                print("Exiting client.")
                break

        # Ask for vehicle ID
        vehicle_id = input("\nEnter vehicle ID: ").strip()
        if not vehicle_id:
            print("Vehicle ID cannot be empty. Please try again.")
            continue

        # Retrieve vehicle data
        response = retrieve_vehicle_data(vehicle_id)
        if response.status_code == 200:
            data = response.json()
            print("\n--- Vehicle Data ---")
            print(json.dumps(data["data"], indent=4))
        elif response.status_code == 403:
            error_message = response.json().get("message", "Unknown error")
            print(f"Error: {error_message}")
            session_token = None  # Reset the session token if invalid
        else:
            error_message = response.json().get("message", "Unknown error")
            print(f"Error: {error_message}")


if __name__ == "__main__":
    main()
