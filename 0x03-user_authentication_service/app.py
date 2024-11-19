#!/usr/bin/env python3
from flask import Flask, jsonify, request, abort
from auth import Auth
from db import DB

AUTH = Auth()
app = Flask(__name__)

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def users(email, password):
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400)
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": "{}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
