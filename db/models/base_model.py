import json

class BaseModel(dict):

    def dict(self):
        return self.__dict__