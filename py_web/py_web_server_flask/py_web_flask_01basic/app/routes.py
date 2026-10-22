from flask import Blueprint, jsonify, redirect, render_template, request
from .database import get_all_users, add_user

api = Blueprint("api", __name__)

VALID_USERNAME = "Admin"
VALID_PASSWORD = "Pass123!"


@api.route("/")
def index():
    return render_template("index.html")


@api.route("/login", methods=["GET", "POST"])
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


# @api.route("/api/users", methods=["GET"])
# def get_users():
#     users = [
#         {"id": 1, "name": "John"},
#         {"id": 2, "name": "Jane"},
#         {"id": 3, "name": "Robert"},
#     ]
#
#     return jsonify(users)
@api.route("/api/users", methods=["GET"])
def get_users():
    users = get_all_users()
    return jsonify(users), 200


@api.route("/api/books", methods=["GET"])
def get_books():
    users = [
        {"id": 1, "name": "ABC", "edition": "NYT"},
        {"id": 11, "name": "ABC11", "edition": "NYT11"},
        {"id": 13, "name": "ABC13", "edition": "NYT13"},
    ]

    return jsonify(users)


@api.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required."}), 400

    first_name = str(data.get("first_name") or "").strip()
    last_name = str(data.get("last_name") or "").strip()
    email = str(data.get("email") or "").strip()
    city = str(data.get("city") or "").strip() or None

    if not first_name or not last_name or not email:
        return (
            jsonify(
                {"error": "First name, last name, and email are required."}
            ),
            400,
        )

    if (
        len(first_name) > 50
        or len(last_name) > 50
        or len(email) > 100
        or (city is not None and len(city) > 50)
    ):
        return (
            jsonify(
                {"error": "One or more fields exceed the allowed length."}
            ),
            400,
        )

    try:
        user_id = add_user(
            first_name,
            last_name,
            email,
            city,
        )
    except ValueError as error:
        return jsonify({"error": str(error)}), 409

    return (
        jsonify(
            {
                "message": "User created successfully.",
                "UserID": user_id,
            }
        ),
        201,
    )
