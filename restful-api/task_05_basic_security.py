#!/usr/bin/python3
"""
Task 5: API Security and Authentication
Implements Basic Auth and JWT authentication with role-based access control
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)

# Initialize Flask application
app = Flask(__name__)
# Initialize Basic Authentication
auth = HTTPBasicAuth()
# Configure JWT secret key (Note: In production, use a strong, unique key)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# In-memory user database with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),  # Hashed password
        "role": "user"  # Regular user role
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),  # Hashed password
        "role": "admin"  # Admin role
    },
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify username/password combination for Basic Authentication
    Args:
        username: Provided username
        password: Provided password
    Returns:
        User object if valid, None otherwise
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Basic Auth protected endpoint
    Returns:
        Success message if authenticated
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """
    JWT Token generation endpoint
    Returns:
        JWT token if credentials are valid
        400 if missing credentials
        401 if invalid credentials
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Validate presence of credentials
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    
    user = users.get(username)
    
    # Verify credentials
    if user and check_password_hash(user["password"], password):
        # Create JWT token with user identity
        access_token = create_access_token(
            identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    JWT protected endpoint
    Returns:
        Success message if valid JWT provided
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Admin-only endpoint protected by JWT and role check
    Returns:
        Success message if admin
        403 if not admin
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing/invalid token cases"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token format cases"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token cases"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token cases"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle cases requiring fresh token"""
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
