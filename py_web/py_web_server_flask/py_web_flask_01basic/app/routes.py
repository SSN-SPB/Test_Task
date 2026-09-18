from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def home():
    return "Starting Page"


@api.route("/api/health", methods=["GET"])
def health_check():
    return jsonify(
        {
            "status": "ok",
            "service": "flask-training",
        }
    )


@api.route("/api/users", methods=["GET"])
def get_users():
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
        {"id": 3, "name": "Robert"},
    ]

    return jsonify(users)
