#!/bin/sh

set -e

echo "Starting address report generation..."

python /app/app.py

echo "HTML report generated successfully."

echo "Starting Nginx..."

exec nginx -g "daemon off;"
