#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies using the requirements file in backend/
pip install -r backend/requirements.txt

# Collect static files
python backend/manage.py collectstatic --noinput

# Run migrations
python backend/manage.py migrate
