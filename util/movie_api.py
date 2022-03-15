import requests as r
import os
from . import env
BASE_URL = 'https://api.themoviedb.org/3/'

def get_now_playing(page = 1):
    url = BASE_URL + 'movie/now_playing?page='+str(page)
    res = r.get(url +'&api_key='+env.movie_api_key)
    return res.json()

def get_top_rated(page = 1):
    url = BASE_URL + 'movie/top_rated?page='+str(page)
    res = r.get(url +'&api_key='+env.movie_api_key)
    return res.json()


# get_now_playing()
