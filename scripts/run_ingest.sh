#!/usr/bin/env bash
cd "$(dirname "$0")/../services/ingest"
cp -n .env.example .env
python3 ingest.py
