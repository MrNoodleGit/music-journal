from flask import Blueprint, jsonify, request


journal_bp = Blueprint("journal", __name__)


@journal_bp.get("/")
def list_entries():
    return jsonify({"items": [], "total": 0})


@journal_bp.post("/")
def create_entry():
    payload = request.get_json(silent=True) or {}
    return jsonify({"id": 1, **payload}), 201


@journal_bp.get("/<int:entry_id>")
def get_entry(entry_id: int):
    return jsonify({"id": entry_id, "title": "stub", "body": "", "tracks": []})


