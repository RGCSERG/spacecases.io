from flask import Flask
from zenora import APIClient
from webstart.config import CLIENT_SECRET, TOKEN , SECRET_KEY
import webstart.database_commands as db
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

db.init()

from webstart import routes