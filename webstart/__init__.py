from flask import Flask
from zenora import APIClient
from webstart.config import CLIENT_SECRET, TOKEN
import webstart.database_commands as db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
Client = APIClient(TOKEN, client_secret=CLIENT_SECRET)
db.init()

from webstart import routes
