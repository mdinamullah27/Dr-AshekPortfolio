#!/bin/bash

# Make migrations
echo "Making migrations..."
python manage.py makemigrations

echo "Migrations created successfully!"
