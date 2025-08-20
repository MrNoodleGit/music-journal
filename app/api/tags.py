from flask import Blueprint, jsonify, request


tags_bp = Blueprint("tags", __name__)


@tags_bp.get("/")
def list_tags():
    return jsonify([{"id": 1, "name": "example"}])


@tags_bp.post("/")
def create_tag():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name", "").strip()
    return jsonify({"id": 2, "name": name}), 201


@tags_bp.post("/assign")
def assign_tag():
    payload = request.get_json(silent=True) or {}
    return jsonify({"assigned": payload}), 200


