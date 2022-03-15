from dotenv import load_dotenv
import os

load_dotenv()

class Env():
    db_username = os.environ.get('DB_USERNAME', 'root')
    db_password = os.environ.get('DB_PASSOWRD', 'root')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', '27017')
    db_dbname = os.environ.get('DB_DBNAME', 'movie_app')
    db_source = os.environ.get('DB_SOURCE', 'admin')
    db_dbalias = os.environ.get('DB_ALIAS', 'movie-app')
    server_host = os.environ.get('SERVER_HOST', 'localhost')
    server_port = os.environ.get('SERVER_PORT', 8080)
    server_mode = os.environ.get('SERVER_MODE', 'debug')
    server_is_debug = server_mode == 'debug'
    movie_api_key = os.environ.get('MOVIE_API_KEY', 'none')
    
env = Env()