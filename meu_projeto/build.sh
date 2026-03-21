#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# O segredo está aqui: apontar para a pasta certa
python projeto_Almoco/manage.py collectstatic --no-input
python projeto_Almoco/manage.py migrate