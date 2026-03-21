#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python projeto_Almoco/manage.py collectstatic --no-input
python projeto_Almoco/manage.py migrate