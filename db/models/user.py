
from .base_model import BaseModel

class User(BaseModel):

    def __init__(self, username, fname, lname, password):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.password = password