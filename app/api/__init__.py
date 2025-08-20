"""Flask blueprints for the API surface."""

from .tracks import tracks_bp
from .tags import tags_bp
from .journal import journal_bp
from .playlists import playlists_bp

__all__ = [
    "tracks_bp",
    "tags_bp",
    "journal_bp",
    "playlists_bp",
]

