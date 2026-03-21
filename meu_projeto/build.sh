#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Se o arquivo está na mesma pasta que o build.sh, o comando é esse:
python manage.py collectstatic --no-input
python manage.py migrate