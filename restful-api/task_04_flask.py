#!/usr/bin/python3
"""
Task 4: Simple RESTful API with Flask
Implements basic CRUD operations for user management
Routes:
    - / : Home endpoint
    - /data : List all usernames
    - /status : API status check
    - /users/<username> : Get user details
    - /add_user : Add new user (POST)
"""

from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# In-memory user database (empty at startup)
users = {}

# Example user data structure (commented out)
"""
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}
"""

@app.route('/')
def home():
    """
    Home endpoint
    Returns:
        str: Welcome message
    """
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def data():
    """
    Get list of all usernames
    Returns:
        JSON: List of usernames
    """
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status', methods=['GET'])
def status():
    """
    API status check
    Returns:
        str: "OK" if API is running
    """
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Get user details by username
    Args:
        username (str): Username to lookup
    Returns:
        JSON: User data if found
        JSON: Error message with 404 if not found
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add new user to the system
    Expects JSON payload with user details
    Returns:
        JSON: Success message and user data (201) if successful
        JSON: Error message (400) if username is missing
    """
    data = request.get_json()

    # Validate required username field
    if not data.get('username'):
        return jsonify({"error": "Username is required"}), 400

    # Add user to database
    users[data['username']] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    # Run Flask development server
    app.run(debug=True)
