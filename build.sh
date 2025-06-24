#!/bin/bash
set -euo pipefail  # Strict mode

echo "=== VERIFYING DATABASE CONNECTION ==="
if [ -z "${DATABASE_URL:-}" ]; then
  echo "❌ CRITICAL ERROR: DATABASE_URL not found!"
  echo "Debug info:"
  echo "--- RENDER ENVIRONMENT ---"
  printenv
  exit 1
fi

echo "=== INSTALLING DEPENDENCIES ==="
pip install -r requirements.txt

echo "=== RUNNING MIGRATIONS ==="
python manage.py migrate --noinput

echo "=== COLLECTING STATIC FILES ==="
python manage.py collectstatic --noinput

echo "✅ SUCCESS: All build steps completed"