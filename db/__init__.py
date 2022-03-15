from flask import current_app, g
from util import env
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

def get_db():

    db = getattr(g, "_database", None)
    if db is None:
        uri = f'mongodb://{env.db_username}:{env.db_password}' \
        f'@{env.db_host}:{env.db_port}/{env.db_dbname}?authSource={env.db_source}'
        db = g._database = PyMongo(current_app, uri=uri).db
    return db

db = LocalProxy(get_db)