from flask import Flask, redirect, url_for, render_template, request, jsonify
from datetime import timedelta
from models import db, User, Files
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({}), 200

@app.route('/login', methods=['POST'])
def login():
    email, password = request.json.get(
            "email", None
        ), request.json.get(
            "password", None
        )
    if not email or not password:
        return "Missing info", 400

    user = User.get_by_email(email)
    if check_password_hash(user.password, password):
        access_token = create_access_token(
            identity=user.to_dict(),
            expires_delta=timedelta(minutes=60)
        )
        return jsonify({'token': access_token}), 200

    return "Invalid info", 400

if __name__ == "__main__":
    app.run()