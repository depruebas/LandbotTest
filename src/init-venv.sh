#!/bin/bash

python -m venv venv
sleep 2
source /var/www/html/venv/bin/activate
sleep 2
pip install -r requirements.txt