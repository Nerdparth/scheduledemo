#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Run Django collectstatic to gather static files
python manage.py collectstatic --noinput

# Run migrations to set up or update the database
python manage.py migrate
