#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mv app/app-config.cfg.dist app/app-config.cfg
mv application.wsgi.dist application.wsgi