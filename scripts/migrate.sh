#!/bin/bash

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "Migrations completed successfully!"
