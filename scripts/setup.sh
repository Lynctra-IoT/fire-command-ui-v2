#!/usr/bin/env bash
set -e
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
python scripts/selftest.py
echo "Backend ready. Run: uvicorn backend.main:app --reload"
