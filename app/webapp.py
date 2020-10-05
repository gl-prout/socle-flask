# Entry point for the application
from app.controllers import Controllers as controllers

from . import app  # For application discovery by the 'flask' command

controllers().grab(app)
