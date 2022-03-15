import json
from db import db
from bson.objectid import ObjectId

class BaseModel():
    
    collection = None

    def __init__(self, _id):
        self._id = _id
        self.serialize_id()

    def dict(self):
        return self.__dict__

    def save(self):
        if hasattr(self, '_id'):
            delattr(self, '_id')
        saved = db[self.get_col()].insert_one(self.dict())
        self._id = saved.inserted_id
        return self

    def serialize_id(self):
        if(isinstance(self._id, ObjectId)):
            self._id = str(self._id)

    @classmethod
    def get_col(cls):
        if cls.collection is None:
            raise Exception('collection was not defined for: ' + cls.__name__)
        return cls.collection

    @classmethod
    def find_by_id(cls, id):
        model = db[cls.get_col()].find_one({'_id': ObjectId(id)})
        if model is None:
            return None
        model = cls(**model)
        model.serialize_id()
        return model
    
    @classmethod
    def find_by_id_or_404(cls, id):
        model = db[cls.get_col()].find_one_or_404({'_id': ObjectId(id)})
        model = cls(**model)
        model.serialize_id()
        return model

    @classmethod
    def find_one_or_404(cls, query_dict):
        model = db[cls.get_col()].find_one_or_404(query_dict)
        model = cls(**model)
        model.serialize_id()
        return model