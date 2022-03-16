from audioop import add
from flask import g, Blueprint, render_template, request, jsonify, Response
from db import db
import json
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
from db.models.user import User
import util.movie_api as api
from flask_login import login_required, current_user
from db.models.fav_movie import FavMovie

movies_bp = Blueprint('movies', __name__, template_folder='templates')

@movies_bp.get('/dashboard/')
@login_required
def dashboard():
    args = request.args
    now_playing_page = args.get('nowPlayingPage') or 1
    top_rated_page = args.get('topRatedPage') or 1
    
    now_playing = api.get_now_playing(now_playing_page)
    top_rated = api.get_top_rated(top_rated_page)

    favorites = FavMovie.find_many({'user_id': current_user._id}, True)
    fav_movie_ids = [f.movie_id for f in favorites]

    return render_template('movies.html', 
        now_playing=now_playing, top_rated=top_rated, username=current_user.username,
        top_rated_page=int(top_rated_page),
        now_playing_page=int(now_playing_page),
        favorite_ids=fav_movie_ids)


@movies_bp.post('/add-fav')
@login_required
def add_to_fav():
    remove = request.args.get('remove') or None
    user_id = current_user._id
    data = request.json
    if not 'movie_id' in data:
        return jsonify({'message': 'Movie id is required'}), 400
    movie_id = data['movie_id'] or None
    movie_id = int(movie_id)  
    movie = api.get_by_id(movie_id)
    fav = FavMovie.find_one({'movie_id': movie_id, 'user_id': current_user._id})
    if (fav is not None) and (remove == 1):
        fav.delete()
    elif fav is None:
        FavMovie(movie_id=movie_id, user_id=user_id, title=movie['original_title'], overview=movie['overview']).save()
    return jsonify({}), 204
