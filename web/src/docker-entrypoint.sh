#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
/opt/conda/envs/rdkit-env/bin/python3 manage.py makemigrations; \
/opt/conda/envs/rdkit-env/bin/python3 manage.py migrate; \
/opt/conda/envs/rdkit-env/bin/python3 manage.py collectstatic --noinput; \
/opt/conda/envs/rdkit-env/bin/python3 manage.py population 
exec "$@"

/opt/conda/envs/rdkit-env/bin/gunicorn \
    PeptideBuilder.wsgi \
    --bind 0.0.0.0:8000 \
    --timeout 600 \
    --workers 4 \
