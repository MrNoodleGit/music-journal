from flask import Blueprint, jsonify, request


tracks_bp = Blueprint("tracks", __name__)


@tracks_bp.get("/")
def list_tracks():
    return jsonify({"items": [], "total": 0})


@tracks_bp.get("/<int:track_id>")
def get_track(track_id: int):
    return jsonify({
        "id": track_id,
        "title": "stub",
        "artist": "stub",
        "tags": [],
        "energy": None,
        "mood": None,
        "notes": None,
    })


@tracks_bp.post("/<int:track_id>/metadata")
def update_track_metadata(track_id: int):
    payload = request.get_json(silent=True) or {}
    # In the future, validate and persist metadata
    return jsonify({"id": track_id, "updated": payload}), 200


