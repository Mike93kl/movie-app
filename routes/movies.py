from flask import g, Blueprint, render_template, request, jsonify, Response
from db import db
import json
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
from db.models.user import User
from util.movie_api import get_by_id, get_now_playing, get_top_rated
from flask_login import login_required, current_user
from db.models.fav_movie import FavMovie

movies_bp = Blueprint('movies', __name__, template_folder='templates')

@movies_bp.get('/dashboard')
@login_required
def dashboard():
    print('dashboard')
    args = request.args
    now_playing_page = args.get('now_playing_page') or 1
    top_rated_page = args.get('top_rated_page') or 1
    
    now_playing = get_now_playing(now_playing_page)
    top_rated = get_top_rated(top_rated_page)
    # get users favorites
    return render_template('movies.html', now_playing=now_playing, top_rated=top_rated, username=current_user.username)

@movies_bp.post('/add-fav')
@login_required
def add_to_fav():
    user_id = current_user._id
    movie_id = request.get_json()['movie_id'] or None
    if movie_id is None:
        return jsonify({'message': 'Movie id is required'}), 400
    movie = get_by_id(movie_id)
    movie_id = movie['movie_id']
    FavMovie(movie_id=movie_id, user_id=user_id).save()
    return jsonify({}), 204