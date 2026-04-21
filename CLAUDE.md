# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Livract** is a social reading platform that centralizes literary discussions and simplifies book recommendation sharing among literature enthusiasts.

## Commands

### Docker (recommended for full-stack dev)
```bash
docker-compose up --build          # first run or after dependency changes
docker-compose up                  # subsequent runs
docker-compose down                # stop all services
docker-compose exec backend pytest                                           # all backend tests in container
docker-compose exec backend pytest tests/path/test_file.py::test_name       # single test in container
docker-compose exec frontend npx vitest run                                  # all frontend tests in container
```

### Backend (FastAPI) — local
```bash
cd backend
uvicorn main:app --reload          # dev server (port 8000)
pip install -r requirements.txt    # install deps
pytest                             # all tests
pytest tests/path/test_file.py::test_name   # single test
```

### Frontend (Next.js) — local
```bash
cd frontend
npm run dev                        # dev server (port 3000)
npm run build && npm run start     # production build
npm run lint                       # lint
npx vitest                         # all tests (watch mode)
npx vitest run src/path/file.test.tsx   # single test file
npx vitest --ui                    # visual test suite in browser
```

## Stack

- **Backend**: FastAPI + Pydantic v2 (Python)
- **Frontend**: Next.js (App Router) + TypeScript
- **Database**: PostgreSQL
- **Auth**: JWT via httpOnly cookie (issued and validated by FastAPI)
- **Dev environment**: Docker Compose

## Architecture

### Backend structure
Each domain is a self-contained module under `backend/<domain>/`:
- `models.py` — SQLAlchemy ORM models
- `schemas.py` — Pydantic request/response schemas
- `routes.py` — FastAPI router

`backend/main.py` is the entry point — it creates the app and registers all routers.
`backend/auth/dependencies.py` exposes `get_current_user`, a FastAPI dependency injected into any route that requires authentication.

### Frontend structure
- `app/` — Next.js App Router pages and layouts
- `components/` — UI components, co-located with their tests (`Component.test.tsx`)
- `lib/` — API clients, TypeScript types, and utilities

API calls live in `lib/` — components never call the backend directly.

### Auth flow
1. `POST /auth/login` returns a signed JWT set as an httpOnly cookie
2. Browser automatically includes the cookie on every subsequent request
3. FastAPI reads the token from the `Cookie` header (not `Authorization`)
4. Protected routes declare `current_user: User = Depends(get_current_user)`
5. `POST /auth/logout` clears the cookie server-side

Frontend never reads the token. CSRF protection is required on all state-mutating endpoints.

## Testing

### Backend (pytest)
- Test files mirror source structure: `backend/tests/<domain>/test_<module>.py`
- Shared fixtures (test client, DB session, auth helpers) live in `backend/conftest.py`
- Use `TestClient` from `fastapi.testclient` for route tests
- Use `app.dependency_overrides[get_db]` in `conftest.py` to inject a dedicated test database session (separate test DB or rolled-back transactions) — never the dev DB
- Authenticated route tests inject a test JWT cookie directly via the test client

### Frontend (Vitest + React Testing Library)
- Test files co-located with components: `components/foo/Foo.test.tsx`
- Test behaviour, not implementation — query by role/label, not CSS selectors
- Mock `next/navigation` globally in Vitest setup for components relying on router hooks
- API calls in `lib/` are mocked at the module boundary in tests
- Run `npx vitest --ui` during active development for live feedback

## Domain Concepts

Key entities to keep consistent across layers:

- **User** — reader profile with preferences and reading history
- **Book** — canonical book record (title, author, ISBN, cover)
- **Reading** — a user's personal record of reading a book (status: want-to-read / reading / finished)
- **Review** — written opinion attached to a Reading
- **Recommendation** — a user directing a Book to one or more friends
- **Discussion** — threaded conversation anchored to a Book or Reading
