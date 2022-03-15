from flask import g, Blueprint, render_template, request, jsonify, Response
from db import db
import json
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
from db.models.user import User
from util.movie_api import get_now_playing, get_top_rated

movies_bp = Blueprint('movies', __name__, template_folder='templates')

@movies_bp.get('/')
def list_movies():
    args = request.args
    now_playing_page = args.get('now_playing_page') or 1
    top_rated_page = args.get('top_rated_page') or 1
    
    now_playing = get_now_playing(now_playing_page)
    top_rated = get_top_rated(top_rated_page)
    # get users favorites
    return render_template('movies.html', now_playing=now_playing, top_rated=top_rated)