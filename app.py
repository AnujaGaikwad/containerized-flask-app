from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    return jsonify({
        "message": "CloudOps Flask API is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/info")
def info():
    return jsonify({
        "application": "CloudOps Flask API",
        "version": "1.0",
        "environment": APP_ENV
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)