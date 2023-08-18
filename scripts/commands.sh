#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py makemigrations --noinput
python manage.py migrate --noinput

if [ "$DEBUG" = "1" ]; then 
    echo 'DEBUB MODE ACTIVATED'

  docker exec python manage.py shell -c "from core.utils.seed_dev import SeedDevInitial; from accounts.models import User; x = SeedDevInitial().execute() if len (User.objects.all()) == 0 else SeedDevInitial().execute()"
fi

python manage.py runserver 0.0.0.0:8000