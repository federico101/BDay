from flask import Flask

def app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "SECRET_KEY"
    
    from .routes import main
    
    app.register_blueprint(main)
    
    return app
