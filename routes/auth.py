from flask import g, Blueprint, render_template, request, jsonify, Response
from db import db
import json
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
from db.models.user import User

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.get('/')
def login():
    return render_template('login.html')

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
        username=username, password=pbkdf2_sha256.hash(password))
    db.users.insert_one(user.dict())
    return jsonify({}), 204
    
    