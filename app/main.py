from flask import Flask, jsonify
from flask_cors import CORS


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

    return app


app = create_app()

