# Fire Command V2 – Project Skeleton (Phase 1)

This repository contains the initial scaffold for the Fire‑Command V2 system.

## Layout

```
backend/      FastAPI service (Python 3.10+)
frontend/     React 18 + Vite web UI
scripts/      Developer helpers
```

## Quick start (dev)

```bash
# ----- backend -----
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
python scripts/selftest.py   # import‑checks
uvicorn backend.main:app --reload

# ----- frontend -----
cd frontend
npm install
npm run dev
```

---

*Phase 1 delivers a “hello world” backend, a minimal React skeleton, and tooling to catch missing dependencies. Subsequent phases will flesh out models, auth, real‑time features, and device ingestion.*

## Frontend (React)

```bash
cd frontend
npm install
npm run dev
# opens http://localhost:5173
```

The dev server proxies `/api/*` to `http://127.0.0.1:8000`, so run the backend locally first.
