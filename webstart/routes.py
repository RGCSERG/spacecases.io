from webstart import app, Client, db
from zenora import APIClient
from webstart.config import REDIRECT_URI, OAUTH_URL, CLIENT_SECRET, TOKEN, INVITE_URL
from webstart.calculations import check_permissions
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
    session['user_code'] = request.args['code']
    access_token = Client.oauth.get_access_token(
        code, REDIRECT_URI).access_token
    session['token'] = access_token
    session.permanent = True
    return redirect('/set')


@app.route('/leaderboard')
def leaderboard():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        user_data: dict = db.user_data.find_one({"_id": current_user.id})
        return render_template('leaderboard.html', current_user=current_user, user_data=user_data)
    return render_template('leaderboard.html', oauth_url=OAUTH_URL)


@app.route('/invite_server')
def invite_server():
    if 'token' in session:
        guilds = []
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        gs = bearer_client.users.get_my_guilds()
        for guild in gs:
            if check_permissions(guild) == True:
                guilds.append(guild)
        return render_template('invite_Server.html', current_user=current_user, guilds=guilds, invite_url=INVITE_URL, str=str)
    return render_template('invite_server.html', oauth_url=OAUTH_URL, invite_url=INVITE_URL)


@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


@app.route('/set')
def set_cookie():
    resp = make_response('Remembering User')
    resp.set_cookie('token', session['token'])
    return resp


@app.route('/get')
def getcookie():
    Client.oauth.refresh_access_token(session['token'])
    if request.cookies.get('token'):
        token = request.cookies.get('token')
        session['token'] = token
        return redirect('/home')
    return redirect('/home')


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