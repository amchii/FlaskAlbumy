from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_login import LoginManager, AnonymousUserMixin
from flask_dropzone import Dropzone
from flask_wtf import CSRFProtect
from flask_avatars import Avatars
from flask_migrate import Migrate
from flask_whooshee import Whooshee

db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
login_manager = LoginManager()
dropzone = Dropzone()
csrf = CSRFProtect()
avatars = Avatars()
migrate = Migrate()
whooshee = Whooshee()


class Guest(AnonymousUserMixin):
    @property
    def is_admin(self):
        return False

    def can(self, permission_name):
        return False


@login_manager.user_loader
def load_user(user_id):
    from albumy.models import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warining'

login_manager.refresh_view = 'auth.re_authenticate'
login_manager.needs_refresh_message_category = 'waring'

login_manager.anonymous_user = Guest
