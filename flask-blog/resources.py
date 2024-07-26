from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models import User, Comment, Post
from api import db

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")
user_args.add_argument('password', type=str, required=True, help="Password cannot be blank")

post_args = reqparse.RequestParser()
post_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
post_args.add_argument('user_id', type=str, required=True, help="Author cannot be blank")
post_args.add_argument('content', type=str, required=True, help="Content cannot be blank")

comment_args = reqparse.RequestParser()
comment_args.add_argument('content', type=str, required=True, help="Content cannot be blank")
comment_args.add_argument('post_id', type=str, required=True, help="Post cannot be blank")
comment_args.add_argument('user_id', type=str, required=True, help="Author cannot be blank")

user_fields = {
    'id':fields.Integer, 
    'name':fields.String, 
    'email':fields.String,
    'password' : fields.String
}

post_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'content': fields.String,
    'date_posted': fields.DateTime, 
    'user_id' : fields.Integer 
}

comment_fields = {
    'id': fields.Integer,
    'content': fields.String,
    'date_posted': fields.DateTime,
    'post_id': fields.Integer,
    'user_id': fields.Integer
}

class UsersResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users
    
    @marshal_with(user_fields)
    def post(self):
        args = user_args.parse_args()
        user = User(name=args['name'], email=args['email'], password=args['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201

class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        return user
    @marshal_with(user_fields)
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        args = user_args.parse_args()
        if not user:
            abort(404)
        user.name = args["name"]
        user.email = args["email"]
        user.password = args["password"]
        db.session.commit()
        return user
    @marshal_with(user_fields)
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404)
        db.session.delete(user)
        db.session.commit()
        users = User.query.all()
        return users, 204


class PostsResource(Resource):
    @marshal_with(post_fields)
    def get(self):
        posts = Post.query.all()
        return posts

    @marshal_with(post_fields)
    def post(self):
        args = post_args.parse_args()
        post = Post(name=args['name'], content=args['content'], user_id=args['user_id'])
        db.session.add(post)
        db.session.commit()
        return post, 201
    
class PostResource(Resource):
    @marshal_with(post_fields)
    def get(self, id):
        post = Post.query.filter_by(id=id).first()
        if not post:
            abort(404, message="Post not found")
        return post

    @marshal_with(post_fields)
    def patch(self, id):
        post = Post.query.filter_by(id=id).first()
        args = post_args.parse_args()
        if not post:
            abort(404)
        post.name = args["name"]
        post.content = args["content"]
        post.user_id = args["user_id"]
        db.session.commit()
        return post
    @marshal_with(post_fields)
    def delete(self, id):
        post = Post.query.filter_by(id=id).first()
        if not post:
            abort(404)
        db.session.delete(post)
        db.session.commit()
        posts = Post.query.all()
        return posts, 204

class CommentsResource(Resource):
    @marshal_with(comment_fields)
    def get(self):
        comments = Comment.query.all()
        return comments

    @marshal_with(comment_fields)
    def comment(self):
        args = comment_args.parse_args()
        comment = Comment(post_id=args['post_id'], content=args['content'], user_id=args['user_id'])
        db.session.add(comment)
        db.session.commit()
        return comment, 201
    
class CommentResource(Resource):
    @marshal_with(comment_fields)
    def get(self, id):
        comment = Comment.query.filter_by(id=id).first()
        if not comment:
            abort(404, message="Comment not found")
        return comment

    @marshal_with(comment_fields)
    def patch(self, id):
        comment = Comment.query.filter_by(id=id).first()
        args = comment_args.parse_args()
        if not comment:
            abort(404)
        comment.post_id = args["post_id"]
        comment.content = args["content"]
        comment.user_id = args["user_id"]
        db.session.commit()
        return comment
    @marshal_with(comment_fields)
    def delete(self, id):
        comment = Comment.query.filter_by(id=id).first()
        if not comment:
            abort(404)
        db.session.delete(comment)
        db.session.commit()
        comments = Comment.query.all()
        return comments, 204