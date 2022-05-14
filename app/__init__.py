from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db.init_app(app)

    @app.before_first_request
    def initialize_database():
        db.create_all()

    
    return app
