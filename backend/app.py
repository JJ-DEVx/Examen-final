from flask import Flask
from database import db
from flask_cors import CORS
from routes import init_routes
import os

app = Flask(__name__)
CORS(app)

#  Ruta correcta para Render
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/workshops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

init_routes(app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)