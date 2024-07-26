from flask_restful import Api
from flask import  jsonify
from resources import UserResource, UsersResource, PostResource, PostsResource, CommentResource, CommentsResource
from create_app import app
api = Api(app)

api.add_resource(UsersResource, '/api/users/')
api.add_resource(UserResource, '/api/users/<int:id>')
api.add_resource(PostsResource, '/api/posts/')
api.add_resource(PostResource, '/api/posts/<int:id>')
api.add_resource(CommentsResource, '/api/comments/')
api.add_resource(CommentResource, '/api/comments/<int:id>')

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Resource not found'}), 404


@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'

if __name__ == "__main__":
    app.run(debug=True)



