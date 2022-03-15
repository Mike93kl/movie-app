from dotenv import load_dotenv
import os

load_dotenv()

class Env():
    db_uri = os.environ.get('DB_URI', '')
    server_host = os.environ.get('SERVER_HOST', 'localhost')
    server_port = os.environ.get('SERVER_PORT', 8080)
    server_mode = os.environ.get('SERVER_MODE', 'debug')
    server_is_debug = server_mode == 'debug'
    movie_api_key = os.environ.get('MOVIE_API_KEY', 'none')
    secret_key = os.environ.get('SECRET_KEY', 'a-secret')
    
env = Env()