#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp app/app-config.cfg.dist app/app-config.cfg
cp application.wsgi.dist application.wsgi