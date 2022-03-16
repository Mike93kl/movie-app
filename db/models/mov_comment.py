from .base_model import BaseModel

class MovComment(BaseModel):

    collection = 'mov_comments'

    def __init__(self, user_id, movie_id, username, comment, _id = None):
        super().__init__(_id)
        self.user_id=user_id
        self.username = username
        self.movie_id=movie_id
        self.comment=comment
