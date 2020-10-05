from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt

db = MongoEngine()
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_pyfile('app-config.cfg')

db.init_app(app)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run()
