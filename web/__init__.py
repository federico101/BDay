from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_name = 'temp.db'

def app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "SECRET_KEY"
    app.config['SQLALCHEMY_DATABASE'] = f"sqlite:///{{db_name}}"
    app.config["SQLALCHEMY_DATABASE_URI"] = "DATABASE_URI"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    
    from .routes import main
    
    app.register_blueprint(main)
    
    from .models import User
    
    return app
