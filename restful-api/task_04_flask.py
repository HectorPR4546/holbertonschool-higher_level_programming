#!/usr/bin/python3
"""
Task 4: Simple API using Flask.
Handles GET/POST requests, serves JSON, and manages user data.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    
    data = request.get_json()
    
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
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
