from .auth import auth_bp
from .movies import movies_bp

def init_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(movies_bp, url_prefix='/movies')
    print('registered')
