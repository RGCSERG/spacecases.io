from flask import Flask
from zenora import APIClient
from .config import Config_data, _blueprint_config_data
import webstart.database_commands as db
import os


Client = APIClient(
    _blueprint_config_data.TOKEN, client_secret=_blueprint_config_data.CLIENT_SECRET
)


def create_app(config_class=Config_data):
    app = Flask(__name__)
    app.config.from_object(Config_data)
    db.init()

    from .bot_management.routes import bot_management
    from .errors.handlers import errors
    from .main.routes import main
    from .oauth2.routes import oauth2
    from .users.routes import users
    from .pages.routes import pages
    from .cookies.cookies import cookies

    app.register_blueprint(bot_management)
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(oauth2)
    app.register_blueprint(users)
    app.register_blueprint(pages)
    app.register_blueprint(cookies)

    return app
