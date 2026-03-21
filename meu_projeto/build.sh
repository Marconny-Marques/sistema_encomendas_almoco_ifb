#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Adicionamos a segunda pasta projeto_Almoco no caminho
python projeto_Almoco/projeto_Almoco/manage.py collectstatic --no-input
python projeto_Almoco/projeto_Almoco/manage.py migrate