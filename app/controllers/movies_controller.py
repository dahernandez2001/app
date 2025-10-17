from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from services.movies_services import MoviesService
from utils.auth_decorators import role_required
from repositories.users_repository import UserRepository

movies_bp = Blueprint("movies_bp", __name__)

# Lista pública (no auth)
@movies_bp.route("/", methods=["GET"])
def list_movies():
    return jsonify(MoviesService.list_movies()), 200

# Obtener detalle (no auth)
@movies_bp.route("/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = MoviesService.get_movie(movie_id)
    if not movie:
        return jsonify({"msg": "Not found"}), 404
    return jsonify(movie), 200

# Crear (admin only)
@movies_bp.route("/", methods=["POST"])
@jwt_required()
def create_movie():
    claims = get_jwt()
    role = claims.get("role", "")
    if role != "admin":
        return jsonify({"msg": "Forbidden: admin only"}), 403
    data = request.get_json() or {}
    movie = MoviesService.create_movie(data)
    return jsonify(movie), 201

# Actualizar (admin only)
@movies_bp.route("/<int:movie_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_movie(movie_id):
    claims = get_jwt()
    role = claims.get("role", "")
    if role != "admin":
        return jsonify({"msg": "Forbidden: admin only"}), 403
    data = request.get_json() or {}
    updated = MoviesService.update_movie(movie_id, data)
    if not updated:
        return jsonify({"msg": "Not found"}), 404
    return jsonify(updated), 200

# Borrar (admin only)
@movies_bp.route("/<int:movie_id>", methods=["DELETE"])
@jwt_required()
def delete_movie(movie_id):
    claims = get_jwt()
    role = claims.get("role", "")
    if role != "admin":
        return jsonify({"msg": "Forbidden: admin only"}), 403
    ok = MoviesService.delete_movie(movie_id)
    if not ok:
        return jsonify({"msg": "Not found"}), 404
    return jsonify({"msg": "Deleted"}), 200
