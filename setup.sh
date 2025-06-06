#!/usr/bin/env bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod 600 data/library.db 2>/dev/null || true
python run.py