#!/bin/bash
set -euo pipefail

echo "=== ENVIRONMENT DUMP ==="
printenv | sort
echo "======================="

if [ -z "${DATABASE_URL:-}" ]; then
  echo "❌ FATAL: Database connection missing!"
  echo "Debug Checklist:"
  echo "1. Verify database service exists in Render"
  echo "2. Check render.yaml database name matches"
  echo "3. Ensure no typos in environment variables"
  exit 1
fi

echo "=== INSTALLING DEPENDENCIES ==="
pip install -r requirements.txt

echo "=== DATABASE CONNECTION TEST ==="
python -c "
import os, psycopg2
try:
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    print('✅ Database connection successful')
except Exception as e:
    print(f'❌ Connection failed: {e}')
    raise
"

echo "=== RUNNING MIGRATIONS ==="
python manage.py migrate --noinput

echo "=== COLLECTING STATIC FILES ==="
python manage.py collectstatic --noinput

echo "✅ BUILD SUCCESSFUL"