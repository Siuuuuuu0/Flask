from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    from models import User, Post, Comment
    
    with app.app_context():
        db.create_all()
    
    from api import api, initialize_routes
    initialize_routes(api)
    api.init_app(app)
    
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.route('/')
    def home():
        return '<h1>Flask REST API</h1>'
    
    return app
