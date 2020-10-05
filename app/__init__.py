from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt

db = MongoEngine()
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_pyfile('app-config.cfg')

db.init_app(app)

if __name__ == '__main__':
    app.run()
