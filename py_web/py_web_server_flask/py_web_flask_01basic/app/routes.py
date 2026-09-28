from flask import Blueprint, jsonify, redirect, render_template, request

api = Blueprint("api", __name__)

VALID_USERNAME = "Admin"
VALID_PASSWORD = "Pass123!"


@api.route("/")
def index():
    return render_template("index.html")


@api.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return redirect("/data")

    return render_template(
        "index.html",
        error="Invalid username or password",
    )


@api.route("/data")
def data():
    return render_template("data.html")


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
