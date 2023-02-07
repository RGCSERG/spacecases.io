from flask import Flask
from zenora import APIClient
from webstart.config import CLIENT_SECRET, TOKEN

app = Flask(__name__)
Client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

from webstart import routes
