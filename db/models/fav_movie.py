from .base_model import BaseModel
class FavMovie(BaseModel):
    
    collection = 'fav_movies'

    def __init__(self, movie_id, user_id):
        self.movie_id = movie_id
        self.user_id = user_id