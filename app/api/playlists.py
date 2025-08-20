from flask import Blueprint, jsonify, request


playlists_bp = Blueprint("playlists", __name__)


@playlists_bp.post("/generate")
def generate_playlist():
    payload = request.get_json(silent=True) or {}
    # In the future, evaluate rules and return tracks
    return jsonify({"rules": payload, "tracks": []})


@playlists_bp.post("/export")
def export_playlist():
    payload = request.get_json(silent=True) or {}
    # In the future, export to Spotify
    return jsonify({"exported": True, "details": payload}), 201


