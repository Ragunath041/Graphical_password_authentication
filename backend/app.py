from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import bcrypt
import os
from dotenv import load_dotenv
import random
import string

load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['graphical_auth']
users = db['users']

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.json
        print("Received registration data:", data)  # Debug print

        # Check if all required fields are present
        required_fields = ['email', 'username', 'password', 'selected_image', 'pattern']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Validate email format
        if not data['email'] or '@' not in data['email']:
            return jsonify({'error': 'Invalid email format'}), 400

        # Check if email already exists
        existing_user = users.find_one({'email': data['email']})
        if existing_user:
            return jsonify({'error': 'Email already registered'}), 409  # Using 409 Conflict for duplicate

        # Hash the password before storing
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        # Create user document
        user = {
            'email': data['email'].lower(),  # Store email in lowercase
            'username': data['username'],
            'password': hashed_password,
            'selected_image': data['selected_image'],
            'pattern': data['pattern']
        }

        # Insert user into database
        result = users.insert_one(user)
        
        if result.inserted_id:
            return jsonify({'message': 'Registration successful'}), 201
        else:
            return jsonify({'error': 'Failed to insert user'}), 500

    except Exception as e:
        print(f"Registration error: {str(e)}")
        return jsonify({'error': f'Registration failed: {str(e)}'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        print("Received login data:", data)  # Debug print

        # Check if email exists in request
        if 'email' not in data:
            return jsonify({'error': 'Email is required'}), 400

        # Find user by email
        user = users.find_one({'email': data['email']})
        print("Found user:", user)  # Debug print

        if not user:
            return jsonify({'error': 'User not found'}), 404

        # If password is provided, verify it
        if 'password' in data:
            if not bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
                return jsonify({'error': 'Invalid password'}), 401

            # If pattern is also provided, verify it
            if 'pattern' in data:
                stored_pattern = user['pattern']
                submitted_pattern = data['pattern']

                if stored_pattern == submitted_pattern:
                    return jsonify({
                        'message': 'Login successful',
                        'username': user['username']
                    }), 200
                else:
                    return jsonify({'error': 'Invalid pattern'}), 401

            # If only password is provided, return the stored image
            return jsonify({
                'selected_image': user['selected_image']
            }), 200

        # If neither password nor pattern is provided, just return the stored image
        return jsonify({
            'selected_image': user['selected_image']
        }), 200

    except Exception as e:
        print(f"Login error: {str(e)}")
        return jsonify({'error': f'Login failed: {str(e)}'}), 500

@app.route('/api/user', methods=['GET'])
def get_user():
    email = request.args.get('email')
    user = users.find_one({'email': email}, {'_id': 0})

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user), 200

# Generate a random 6-digit OTP
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

@app.route('/api/generate-otp', methods=['POST'])
def generate_otp_route():
    try:
        data = request.json
        if 'email' not in data:
            return jsonify({'error': 'Email is required'}), 400

        # Generate a new OTP
        otp = generate_otp()
        
        # In a real application, you would send this OTP via email/SMS
        # For demo purposes, we'll just return it
        return jsonify({
            'message': 'OTP generated successfully',
            'otp': otp
        }), 200

    except Exception as e:
        print(f"OTP generation error: {str(e)}")
        return jsonify({'error': f'Failed to generate OTP: {str(e)}'}), 500

@app.route('/api/verify-otp', methods=['POST'])
def verify_otp():
    try:
        data = request.json
        if not all(k in data for k in ['email', 'otp', 'expected_otp']):
            return jsonify({'error': 'Email, OTP, and expected OTP are required'}), 400

        # Simple verification - compare the OTPs
        if data['otp'] == data['expected_otp']:
            return jsonify({'message': 'OTP verified successfully'}), 200
        else:
            return jsonify({'error': 'Invalid OTP'}), 401

    except Exception as e:
        print(f"OTP verification error: {str(e)}")
        return jsonify({'error': f'Failed to verify OTP: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
