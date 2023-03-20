from webstart import app, Client, db
from webstart.database_commands import get_leaderboard
from zenora import APIClient, OauthResponse, OauthAPI
from webstart.config import REDIRECT_URI, OAUTH_URL, CLIENT_SECRET, TOKEN, INVITE_URL
from webstart.calculations import permissions, iscasesin, updateLD
from flask import render_template, url_for, flash, redirect, request, session, make_response
from datetime import timedelta, datetime


@app.route('/')
def check_for_user():
    return redirect('/get')


@app.route('/home')
def home():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('home.html', current_user=current_user)

    return render_template('home.html', oauth_url=OAUTH_URL)


@app.route('/oauth/callback')
def callback():
    code = request.args['code']
    resp = Client.oauth.get_access_token(code,REDIRECT_URI)
    session['token'] = resp.access_token
    session['refresh_token'] = resp.refresh_token
    session.permanent = True
    cookie_set = make_response(redirect('/home'))
    cookie_set.set_cookie('tokens', resp.access_token + ':' + resp.refresh_token)

    return cookie_set


@app.route('/leaderboard')
def leaderboard():
    Leaderboard = updateLD(Client, get_leaderboard, db)
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        gs = bearer_client.users.get_my_guilds()
        guilds = [guild for guild in gs if iscasesin(guild) == True]
        return render_template('leaderboard.html', oauth_url=OAUTH_URL, Leaderboard=Leaderboard, current_user=current_user, guilds = guilds , str=str)
    return render_template('leaderboard.html', oauth_url=OAUTH_URL, Leaderboard=Leaderboard, Client=Client)


@app.route('/invite_server')
def invite_server():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        gs = bearer_client.users.get_my_guilds()
        guilds = [guild for guild in gs if permissions(guild) == True]
        return render_template('invite_Server.html', current_user=current_user, guilds=guilds, invite_url=INVITE_URL, str=str)
    return render_template('invite_server.html', oauth_url=OAUTH_URL, invite_url=INVITE_URL)


@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.route('/get')
def getcookie():
    if request.cookies.get('tokens'):
        refresh_token = request.cookies.get('tokens').split(':')[1]
        resp = Client.oauth.refresh_access_token(refresh_token)
        session['token'] = resp.access_token
        return redirect('/home')
    return redirect('/home')

@app.route('/profile')
def profile():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('profile.html', current_user=current_user)

    return render_template('profile.html', oauth_url=OAUTH_URL)


@app.route('/test')
def test():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('test.html', current_user=current_user)

    return render_template('test.html', oauth_url=OAUTH_URL)


@app.errorhandler(400)
def page_not_found(e):
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('400.html', current_user=current_user)
    return render_template('400.html', oauth_url=OAUTH_URL)


@app.errorhandler(401)
def page_not_found(e):
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('401.html', current_user=current_user)
    return render_template('401.html', oauth_url=OAUTH_URL)


@app.errorhandler(403)
def page_not_found(e):
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('403.html', current_user=current_user)
    return render_template('403.html', oauth_url=OAUTH_URL)


@app.errorhandler(404)
def page_not_found(e):
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('404.html', current_user=current_user)
    return render_template('404.html', oauth_url=OAUTH_URL)


@app.errorhandler(500)
def page_not_found(e):
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('500.html', current_user=current_user)
    return render_template('500.html', oauth_url=OAUTH_URL)
