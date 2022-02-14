# Entry point for the application
from app.controllers import Controllers as Ctrl

from . import app  # For application discovery by the 'flask' command

Ctrl().grab(app)
