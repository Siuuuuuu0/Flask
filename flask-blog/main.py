from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from __init__ import db
from models import User, Post, Comment


main = Blueprint('main', __name__)

@login_required
@main.route('/profile')
def profile():
    return render_template('profile.html', user=current_user)

@main.route('/add_post', methods=['POST'])
@login_required
def add_post():
    name = request.form.get('name')
    content = request.form.get('content')
    user_id = current_user.id
    post = Post(name=name, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('main.profile'))

@main.route('/post/<int:post_id>')
@login_required
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@main.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    content = request.form.get('content')
    post_id = request.form.get('post_id')
    user_id = request.form.get('user_id')
    comment = Comment(content=content, post_id=post_id, user_id=user_id)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.view_post', post_id=post_id))
