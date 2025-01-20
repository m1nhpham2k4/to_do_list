from flask import Flask
import os
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

db = SQLAlchemy()

load_dotenv()
SECREAT_KEY = os.environ.get("KEY")
DB_NAME = os.environ.get("DB_NAME")

print(SECREAT_KEY)

def create_database(app):
    with app.app_context():
        if not os.path.exists('todolist/' + DB_NAME):
            db.create_all()
            print('Created Database!')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECREAT_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Tạo file DB_NAME cùng cấp
    db.init_app(app)

    from .model import Note, User

    create_database(app)
    from todolist.user import user
    from todolist.views import views
    app.register_blueprint(user)
    app.register_blueprint(views)

    login_manager = LoginManager()
    login_manager.login_view='user.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app
