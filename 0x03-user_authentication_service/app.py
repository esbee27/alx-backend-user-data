#!/usr/bin/env python3
from flask import Flask, jsonify
from auth import Auth

AUTH = Auth()
app = Flask(__name__)

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def users(email, password):
    user =


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
