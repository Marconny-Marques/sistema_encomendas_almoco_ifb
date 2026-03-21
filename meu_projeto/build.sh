#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# O caminho real baseado na sua foto:
python projeto_Almoco/manage.py collectstatic --no-input
python projeto_Almoco/manage.py migrate