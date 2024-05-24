from importlib.resources import Resource
from urllib.parse import urlparse
import datetime
import json
from functools import wraps
import requests
from flask import current_app as app
from flask import request, jsonify
from models.models import db, Users



# register
@app.route("/api_register", methods=["POST"])
def register():
        if request.method == 'POST':
            try:
                data = request.json
                user_name = data['user_name']
                password = data['password']
                confirm_password = data['confirm_password']

                # Check if passwords match
                if password != confirm_password:
                    return jsonify({'error': 'Passwords do not match'}), 400

                existing_user = Users.query.filter_by(user_name=user_name).first()
                if existing_user:
                    return jsonify({'error': 'Username already exists'}), 400

                # Create new user object
                new_user = Users(user_name=user_name, password=password, confirm_password=confirm_password)

                # Add new user to session and commit changes
                db.session.add(new_user)
                db.session.commit()

                return jsonify({'message': 'User registered successfully'}), 201

            except KeyError:
                return jsonify({'error': 'Missing required fields in request'}), 400
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        return jsonify({'error': 'Method not allowed'}), 405


# Login
@app.route("/api_login", methods=["POST"])
def login():
        if request.method == 'POST':
            try:
                data = request.json
                user_name = data['user_name']
                password = data['password']

                # Retrieve user from database by username
                user = Users.query.filter_by(user_name=user_name).first()

                # Check if user exists and password matches
                if user and user.password == password:
                    return jsonify({'message': 'Login successful'}), 200
                else:
                    return jsonify({'error': 'Invalid username or password'}), 401

            except KeyError:
                return jsonify({'error': 'Missing required fields in request'}), 400
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'error': 'Method not allowed'}), 405




