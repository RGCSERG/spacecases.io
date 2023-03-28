
from flask import Flask
from zenora import APIClient
from .config import CLIENT_SECRET, TOKEN , SECRET_KEY, Config
import webstart.database_commands as db
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Client = APIClient(TOKEN, client_secret=CLIENT_SECRET)



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init()

    from .bot_management.routes import bot_management
    from .errors.routes import errors
    from .main.routes import main
    from .oauth2.routes import oauth2
    from .users.routes import users

    app.register_blueprint(bot_management)
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(oauth2)
    app.register_blueprint(users)

    return app
