#!/usr/bin/python3
"""
Task 4: Simple API using Flask.
Handles GET/POST requests, serves JSON, and manages user data.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize empty users dictionary
users = {}

@app.route('/')
def home():
    """Root endpoint returning welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns list of usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns API status."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns user data by username or 404 if not found."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds new user from POST data."""
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    
    data = request.get_json()
    
    # Check for required username field
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    
    # Check for duplicate user (return 400 as specified in requirements)
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    # Create new user with whatever data was provided
    user_data = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }
    
    users[username] = user_data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
