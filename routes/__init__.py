from .auth import auth_bp
from .movies import movies_bp
from flask_login import current_user as user
from flask import redirect

def init_routes(app):

    @app.get('/')
    def index():
        return redirect('/movies/dashboard' 
            if user.is_authenticated else '/auth/login')

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(movies_bp, url_prefix='/movies')