from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from services.users_services import UserService

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "user")  # opcional: permitir crear admin si quieres
    return UserService.register_user(username, password, role)

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    user = UserService.authenticate_user(username, password)
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    additional_claims = {"role": user.role}
    access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
    refresh_token = create_refresh_token(identity=user.id, additional_claims=additional_claims)

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200

@user_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    # Puedes regenerar claims desde DB si quieres
    # user = UserRepository.find_by_id(identity)
    access_token = create_access_token(identity=identity)
    return jsonify({"access_token": access_token}), 200
