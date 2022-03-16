from .base_model import BaseModel
class FavMovie(BaseModel):
    
    collection = 'fav_movies'

    def __init__(self, movie_id, user_id, title, overview= '', poster_url = '',  _id = None):
        super().__init__(_id)
        self.movie_id = movie_id
        self.user_id = user_id
        self.title = title
        self.poster_url = poster_url
        self.overview = overview