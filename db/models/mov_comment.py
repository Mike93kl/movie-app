from .base_model import BaseModel

class MovComment(BaseModel):

    collection = 'mov_comments'

    def __ini__(self, user_id, mov_id, comment):
        self.user_id=user_id
        self.movie_id=mov_id
        self.comment=comment
