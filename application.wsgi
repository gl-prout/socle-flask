#!/usr/bin/python3
import sys
PROJECT_DIR = '/var/www/socle_flask/'
sys.path.insert(0, PROJECT_DIR)
from app.webapp import app as application
application.root_path = PROJECT_DIR
