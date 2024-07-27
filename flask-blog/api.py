from flask_restful import Api
from resources import UsersResource, UserResource, PostsResource, PostResource, CommentsResource, CommentResource, UserPostsResource, UserCommentsResource, PostCommentsResource

api = Api()

def initialize_routes(api):
    api.add_resource(UsersResource, '/api/users/')
    api.add_resource(UserResource, '/api/users/<int:id>')
    api.add_resource(PostsResource, '/api/posts/')
    api.add_resource(PostResource, '/api/posts/<int:id>')
    api.add_resource(CommentsResource, '/api/comments/')
    api.add_resource(CommentResource, '/api/comments/<int:id>')
    api.add_resource(UserPostsResource, '/api/users/<int:user_id>/posts')
    api.add_resource(UserCommentsResource, '/api/users/<int:user_id>/comments')
    api.add_resource(PostCommentsResource, '/api/posts/<int:post_id>/comments')




