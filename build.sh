#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

python ./manage.py createsuperuser --username valenzmi --password 123321 --noinput --email 'blank@email.com'

# Apply any outstanding database migrations
python manage.py migrate