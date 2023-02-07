from flask import Flask
from zenora import APIClient
from webstart.config import CLIENT_SECRET, TOKEN

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
Client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

from webstart import routes
