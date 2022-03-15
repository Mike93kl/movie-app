from distutils.log import debug
from flask import Flask
from routes import init_routes
from util import env
from util.movie_api import get_now_playing

app = Flask(__name__)
init_routes(app)

app.run(host=env.server_host, port=env.server_port, debug=env.server_is_debug)