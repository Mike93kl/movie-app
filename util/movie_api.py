import requests as r
import os
from . import env
BASE_URL = 'https://api.themoviedb.org/3/'

def get_now_playing(page = 1):
    url = BASE_URL + 'movie/now_playing?page='+str(page)
    res = get_movie_api(url, '&')
    return res.json()

def get_top_rated(page = 1):
    url = BASE_URL + 'movie/top_rated?page='+str(page)
    res = get_movie_api(url, '&')
    return res.json()


def get_by_id(id):
    url = BASE_URL + 'movie/' + str(id)
    res = get_movie_api(url)
    return res.json()


def get_movie_api(url, q_sep = '?'):
    return r.get(url+q_sep+'api_key='+env.movie_api_key)
