from flask_login import LoginManager
from util import env
from db.models.user import User

def init_managers(app):
    app.config['SECRET_KEY'] = env.secret_key
    login_manager = LoginManager()
    login_manager.login_view='auth.user_login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        print('getting iser ...' + id)
        return User.find_by_id(id)