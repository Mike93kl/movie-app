
from .base_model import BaseModel
from flask_login import UserMixin
from .roles_enum import UserRolesEnum
class User(UserMixin, BaseModel):

    collection = 'users'

    def __init__(self, username, fname, lname, password, role=UserRolesEnum.USER, _id=None):
        super().__init__(_id)
        self.username = username
        self.fname = fname
        self.lname = lname
        self.password = password
        self.role= role

    def get_id(self):
        return self._id
    