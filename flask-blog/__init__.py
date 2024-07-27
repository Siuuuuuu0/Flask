from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    db.init_app(app)

    from models import User, Post, Comment

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    with app.app_context():
        db.create_all()
    
    from api import api, initialize_routes
    initialize_routes(api)
    api.init_app(app)

    from auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.route('/')
    def home():
        return '<h1>Flask REST API</h1>'
    
    return app
