#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "==> Installing dependencies..."
pip install -r backend/requirements.txt

echo "==> Collecting static files..."
python backend/manage.py collectstatic --noinput

echo "==> Running migrations..."
python backend/manage.py migrate

echo "==> Seeding initial portfolio content..."
python backend/manage.py seed_portfolio || true

echo "==> Build finished successfully!"
