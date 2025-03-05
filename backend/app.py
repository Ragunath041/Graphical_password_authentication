from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['graphical_auth']
users = db['users']

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    
    # Check if email already exists
    if users.find_one({'email': data['email']}):
        return jsonify({'error': 'Email already registered'}), 400
    
    # Create user document
    user = {
        'email': data['email'],
        'username': data['username'],
        'selected_image': data['selected_image'],
        'pattern': data['pattern']  # This will be the grid cell numbers
    }
    
    # Insert user into database
    users.insert_one(user)
    
    return jsonify({'message': 'Registration successful'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    
    # Find user by email
    user = users.find_one({'email': data['email']})
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Return the image and verify pattern
    if data.get('pattern'):
        stored_pattern = user['pattern']
        submitted_pattern = data['pattern']
        print(f"Stored pattern: {stored_pattern}")  # Debug log
        print(f"Submitted pattern: {submitted_pattern}")  # Debug log
        
        if stored_pattern == submitted_pattern:
            return jsonify({
                'message': 'Login successful',
                'username': user['username']
            }), 200
        else:
            return jsonify({'error': 'Invalid pattern'}), 401
    
    # First step of login - return the stored image
    return jsonify({
        'selected_image': user['selected_image']
    }), 200

@app.route('/api/user', methods=['GET'])
def get_user():
    email = request.args.get('email')
    user = users.find_one({'email': email}, {'_id': 0})
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
        
    return jsonify(user), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)