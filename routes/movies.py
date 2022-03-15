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
    # get users favorites
    print(len(now_playing['results']))
    return render_template('movies.html', 
        now_playing=now_playing, top_rated=top_rated, username=current_user.username,
        top_rated_page=int(top_rated_page),
        now_playing_page=int(now_playing_page))

@movies_bp.get('/dashboard/movie/<mid>')
@login_required
def get_single_movie(mid):
    mid = int(mid)
    movie = api.get_by_id(str(mid));
    if ('success' in movie) and (movie['success'] == False):
        return render_template('404.html', message='Movie not found')
    
    add_to_fav = request.args.get('addToFavorite') or None
    print(type(add_to_fav))
    if add_to_fav == '1':
        print('in here')
        fav = FavMovie.find_one({
        'user_id': current_user._id,
        'movie_id': mid
        })
        print
        if fav is None:
            FavMovie(movie_id=movie['id'], user_id=current_user._id, title=movie['original_title']).save()
    elif add_to_fav == '0':
        favorite = FavMovie.find_one({
            'user_id': current_user._id,
            'movie_id': mid
        })
        if favorite is not None:
            FavMovie.delete_one({'_id': ObjectId(favorite._id)})
       

    favorite = FavMovie.find_one({
        'user_id': current_user._id,
        'movie_id': mid
    })
    print(favorite is None)
    return render_template('single_movie.html', movie=movie, favorite=favorite.dict())

@movies_bp.post('/add-fav')
@login_required
def add_to_fav():
    user_id = current_user._id
    movie_id = request.get_json()['movie_id'] or None
    if movie_id is None:
        return jsonify({'message': 'Movie id is required'}), 400
    movie = api.get_by_id(movie_id)
    movie_id = movie['movie_id']
    FavMovie(movie_id=movie_id, user_id=user_id, title=movie['original_title']).save()
    return jsonify({}), 204