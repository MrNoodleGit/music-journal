from flask import Flask, jsonify
from flask_cors import CORS
from .api import tracks_bp, tags_bp, journal_bp, playlists_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.update({
        "APP_NAME": "Music Journal API",
        "APP_VERSION": "0.1.0",
    })

    # Allow local development origins; tighten in production.
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.get("/healthz")
    def healthcheck() -> tuple[dict[str, str], int]:
        return {"status": "ok"}, 200

    @app.get("/")
    def root() -> tuple[dict[str, str], int]:
        return {"service": "music-journal", "status": "running"}, 200

    # Register blueprints
    app.register_blueprint(tracks_bp, url_prefix="/tracks")
    app.register_blueprint(tags_bp, url_prefix="/tags")
    app.register_blueprint(journal_bp, url_prefix="/journal")
    app.register_blueprint(playlists_bp, url_prefix="/playlists")

    return app


app = create_app()

