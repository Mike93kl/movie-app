from flask import g, Blueprint, render_template, request, jsonify, Response, redirect, url_for
from db import db
import json
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
from db.models.user import User
from flask_login import login_user, login_required, logout_user

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.get('/login')
def login():
    return render_template('login.html')

@auth_bp.post('/login')
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if (username is None) or (password is None):
        return jsonify({'message': 'Username and password are mandatory!'}), 400
    
    user = User.find_one({'username': username})
    if user is None:
        return render_template('login.html', message="Credentials error")
    if not pbkdf2_sha256.verify(password, user.password):
        return render_template('login.html', message="Credentials error")
    login_user(user, remember=True)
    return redirect('/movies/dashboard')
    

@auth_bp.get('/signup')
def get_signup():
    return render_template('signup.html')

@auth_bp.post('/signup')
def post_signup():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    username = request.form.get('username')
    password = request.form.get('password')
    print(fname, lname, username, password)
    if (fname is None) or (lname is None) or (username is None) \
        or (password is None):
        return jsonify({'message': 'All fields are required'}), 400

   
    user = db.users.find_one({'username': username})
    if user is not None:
        return jsonify({'message': 'Username already taken!'}), 400
    user = User(fname=fname, lname=lname, 
        username=username, password=pbkdf2_sha256.hash(password)).save()
    return jsonify({}), 204

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    