from distutils.log import debug
from flask import Flask, jsonify
from routes import init_routes
from util import env
from managers import init_managers

app = Flask(__name__)
init_routes(app)
init_managers(app)

app.run(host=env.server_host, port=env.server_port, debug=env.server_is_debug)