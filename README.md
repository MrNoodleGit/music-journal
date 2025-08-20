# music-journal

A web-based music library management system that integrates with Spotify to create a personal music journal with enhanced metadata capabilities. The application will allow you to tag songs by themes, add custom descriptions and metadata, track listening history over time, and generate curated playlists based on this enriched data. The system should also support adding non-Spotify tracks to create a comprehensive music database for DJ set preparation and musical experience curation. Built using Python.

Core Features:

- Spotify integration to import and sync your music library
- Custom tagging system and metadata fields for songs (themes, descriptions, mood, energy level)
- Playlist generation based on tags and metadata with filtering options
- Music journal functionality to track listening patterns and experiences over time

## Vision and Goals

Build a personal, searchable, and extensible music knowledge base that:

- Enhances Spotify data with custom metadata and narrative context
- Supports non-Spotify sources for a complete library
- Generates context-aware playlists and setlists
- Surfaces listening patterns and insights over time

## Key Use Cases

- Add rich notes to tracks and albums: descriptions, mood, energy, themes, context
- Tag music (e.g., "sunset", "driving", "deep focus", "warm-up set") and filter easily
- Generate playlists based on tags and numeric attributes (energy, bpm, decade)
- Journal listening sessions, gigs, trips, or moments with music entries
- See trends: favorite tags by month, most journaled artists, mood distribution
- Import/update library from Spotify; support custom uploads/links for non-Spotify tracks

## Functional Requirements (MVP → v1)

- MVP

  - OAuth login with Spotify; read library and basic playback data
  - Core entities: Track, Artist, Album, Tag, JournalEntry, PlaylistTemplate
  - Custom metadata per Track: freeform notes, mood (enum), energy (1-10), bpm (optional), keys, themes (tags)
  - Tagging: create/delete/rename tags; assign tags to tracks
  - Playlist generation from rules (include/exclude tags, min/max energy, optional bpm range)
  - Journal: create entries linking tracks with context (text, date/time, location optional)
  - Basic search: by text, tag, artist, energy
  - Export generated playlist to Spotify

- v1+
  - Non-Spotify track ingestion (file upload or URL metadata-only), waveform/bpm detection (later)
  - Listening history timeline and insights (top tags/artists over periods)
  - Batch editing tools (bulk tag assign, energy normalization)
  - Mobile-friendly UI improvements

## Non-Functional Requirements

- Privacy-first: local database by default; no third-party analytics
- Reliable sync with deduplication and idempotency
- Performant search on medium libraries (10k–50k tracks)
- Testable API with clear contracts

## Proposed Architecture

- Backend: Flask (Python), REST API
- Data: PostgreSQL (prod), SQLite (dev) via SQLAlchemy + Alembic
- Background jobs: on-demand tasks (initially inline), migrate to a worker if needed
- Auth: Spotify OAuth (Authorization Code with PKCE), local session
- Integrations: Spotify Web API (library read, playlist write)
- Frontend: Start with server-rendered pages and simple HTMX/Alpine.js; later, optional React

Directory layout (initial):

```
app/
  main.py            # Flask app entry with health check
  api/               # Blueprints (tracks, tags, playlists, journal)
  models/            # SQLAlchemy models
  schemas/           # Data schemas (optional)
  services/          # Business logic (spotify, playlist rules)
  db/                # Session, migrations config
```

## Initial Data Model (draft)

- User(id, spotify_user_id, display_name)
- Artist(id, name, spotify_id?)
- Album(id, name, spotify_id?, release_year)
- Track(id, title, artist_id, album_id, spotify_id?, duration_ms, bpm?, key?, energy:int, mood:enum, notes:text, created_at)
- Tag(id, name, description?) and TrackTag(track_id, tag_id)
- JournalEntry(id, user_id, occurred_at, title?, body, location?) and JournalEntryTrack(entry_id, track_id, notes?)
- PlaylistTemplate(id, name, rules_json)

Notes:

- Use nullable fields for optional audio features (bpm/key) until source is available
- `rules_json` holds filter config; validate with Pydantic schema

## API Surface (MVP)

- Auth
  - GET /auth/login → redirect to Spotify
  - GET /auth/callback → issue session
- Health
  - GET /healthz
- Tracks
  - GET /tracks?query=&tag=&energy_min=&energy_max=
  - GET /tracks/{id}
  - POST /tracks/{id}/metadata (notes, energy, mood)
- Tags
  - GET /tags, POST /tags, POST /tracks/{id}/tags, DELETE /tracks/{id}/tags/{tagId}
- Journal
  - GET /journal, POST /journal, GET /journal/{id}
- Playlist Generation
  - POST /playlists/generate → returns track list
  - POST /playlists/export → creates Spotify playlist

## Spotify Integration Plan

- Scopes (minimum): user-library-read, playlist-modify-private, playlist-modify-public
- Strategy:
  - First-time import: fetch saved tracks, basic audio features if available
  - Store `spotify_id` for de-duplication; avoid overwriting user metadata on re-sync
  - Export playlists by writing to Spotify and storing mapping to template/run

## Roadmap

1. Foundation (this sprint)

   - Scaffold Flask app with health check
   - Define schemas for Tag, Track, JournalEntry
   - Stub blueprints and services

2. Local Persistence

   - Add SQLAlchemy models and SQLite; create migrations (Alembic)
   - Implement CRUD for Tags and Track metadata

3. Spotify OAuth + Import

   - OAuth flow; store user
   - Import saved tracks and basic features

4. Playlist Rules Engine

   - Define rule schema; implement filtering/weighting
   - Export to Spotify

5. Journal + Insights

   - Journal CRUD and list views
   - Basic insights (tag frequency over time)

6. Non-Spotify Tracks (v1+)
   - Metadata-only records, optional file handling (future)

## Local Development

Prereqs: Python 3.10+ recommended.

1. Create environment and install deps

   - `python3 -m venv .venv && source .venv/bin/activate`
   - `python -m pip install --upgrade pip`
   - `pip install -r requirements.txt`

2. Run the API

   - `flask --app app.main run --debug`
   - Visit `http://localhost:5000/healthz` → `{ "status": "ok" }`

3. Dev notes
   - Add new blueprints under `app/api`
   - Add business logic under `app/services`

## Next Steps

- [x] Add project plan to README
- [x] Scaffold Flask app with health check
- [ ] Add API module structure and placeholder routers
- [ ] Choose DB (SQLite dev, Postgres prod) and wire SQLAlchemy + Alembic
- [ ] Define schemas for Track, Tag, JournalEntry
- [ ] Implement Tag CRUD
- [ ] Implement Track metadata update
- [ ] Implement Spotify OAuth flow
