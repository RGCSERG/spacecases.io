from webstart import app, Client
from webstart.config import REDIRECT_URI, OAUTH_URL, CLIENT_SECRET, TOKEN
from flask import render_template, url_for, flash, redirect, request

@app.route('/')
def home():
    return render_template('index.html', oauth_url=OAUTH_URL)

@app.route('/oauth/callback')
def callback():
    code = request.args['code']
    oauth_response = Client.oauth.get_access_token(code,REDIRECT_URI)
    return oauth_response.access_token