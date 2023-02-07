from webstart import app, Client
from zenora import APIClient
from webstart.config import REDIRECT_URI, OAUTH_URL, CLIENT_SECRET, TOKEN
from flask import render_template, url_for, flash, redirect, request, session

@app.route('/')
def home():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        render_template('index.html', current_user=current_user)

    return render_template('index.html', oauth_url=OAUTH_URL)

@app.route('/oauth/callback')
def callback():
    code = request.args['code']
    access_token = Client.oauth.get_access_token(code,REDIRECT_URI).access_token
    session['token'] = access_token
    return redirect('/')