from webstart import app, Client, db
from .database_commands import get_leaderboard
from zenora import APIClient, OauthResponse, OauthAPI, Snowflake
from zenora.models.snowflake import convert_snowflake
from zenora.exceptions import BadTokenError
from .config import REDIRECT_URI, OAUTH_URL, CLIENT_SECRET, TOKEN, INVITE_URL
from .calculations import permissions, iscasesin, updateLD
from flask import render_template, url_for, flash, redirect, request, session, make_response
from datetime import timedelta, datetime
#instead of using discord ouath to return bot info about user return by batabse ID to save Client acess rate
#release notes page
#Devs page
#second db or rework on leaderboard + remember cookies attr for users + server leaderboards rework
#patreon
#add if statement for invite server
#can remove cookies ask for now
#check if current_user in session works -- can confirm you can't add current_user to json file as it is a class

@app.route('/')
# def check_for_user():
#     return redirect('/get')


@app.route('/spacecases/home')
def home():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('home.html', current_user=current_user)
    except BadTokenError:
        return render_template('home.html', oauth_url=OAUTH_URL)
    return render_template('home.html', oauth_url=OAUTH_URL)


@app.route('/oauth/callback')
def callback():
    code = request.args['code']
    resp = Client.oauth.get_access_token(code,REDIRECT_URI)
    session['token'] = resp.access_token
    session['refresh_token'] = resp.refresh_token
    session.permanent = True
    # cookie_set = make_response(redirect('/spacecases/home'))
    # cookie_set.set_cookie('tokens', resp.access_token + ':' + resp.refresh_token + ':' + resp.scope  + ':' + resp.token_type)

    return redirect('/spacecases/home')


@app.route('/spacecases/leaderboard')
def leaderboard():
    Leaderboard, status = updateLD(Client, get_leaderboard, db)
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            guilds = iscasesin(bearer_client.users.get_my_guilds(), Client.users.get_my_guilds())
            return render_template('leaderboard.html',oauth_url=OAUTH_URL,Leaderboard=Leaderboard,current_user=current_user,guilds=guilds,str=str,len=len,interate=status) # remove [:10] when updateLD is fixed and not using setlist
    except BadTokenError:
        return render_template('leaderboard.html',oauth_url=OAUTH_URL,Leaderboard=Leaderboard,len=len,iterate=status) # remove [:10] when updateLD is fixed and not using setlist
    return render_template('leaderboard.html',oauth_url=OAUTH_URL,Leaderboard=Leaderboard,len=len,iterate=status) # remove [:10] when updateLD is fixed and not using setlist



@app.route('/spacecases/invite_server')
def invite_server():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            guilds = permissions(bearer_client.users.get_my_guilds())
            return render_template('invite_Server.html', current_user=current_user, guilds=guilds, invite_url=INVITE_URL, str=str)
    except BadTokenError:
        return render_template('invite_server.html', oauth_url=OAUTH_URL, invite_url=INVITE_URL)
    return render_template('invite_server.html', oauth_url=OAUTH_URL, invite_url=INVITE_URL)



@app.route('/spacecases/logout')
def logout():
    session.clear()
    return redirect("/")

# @app.route('/spacecases/get')
# def getcookie():
#     if request.cookies.get('tokens'):
#         refresh_token = request.cookies.get('tokens').split(':')[1]
#         access_token = request.cookies.get('tokens').split(':')[0]
#         resp = Client.oauth.refresh_access_token(refresh_token)
#         session['token'] = resp.access_token
#         try:
#             resp = Client.oauth.refresh_access_token(refresh_token)
#             session['token'] = resp.access_token
#         except KeyError:
#             return redirect('/spacecases/home')
#         try:
#             session['token'] = access_token
#             bearer_client = APIClient(session.get('token'), bearer=True)#
#         except BadTokenError:
#             return redirect('/spacecases/home')

@app.route('/spacecases/profile')
def profile():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('profile.html', current_user=current_user)
    except BadTokenError:
        return render_template('profile.html', oauth_url=OAUTH_URL)
    return render_template('profile.html', oauth_url=OAUTH_URL)

@app.route('/spacecases/socials')
def socials():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('profile.html', current_user=current_user)

    return render_template('profile.html', oauth_url=OAUTH_URL)

@app.route('/spacecases/premium')
def premium():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('profile.html', current_user=current_user)

    return render_template('profile.html', oauth_url=OAUTH_URL)

@app.route('/spacecases/release_notes/<str:version>')
def releasenotes(version):
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('releasenotes.html', current_user=current_user)
    except BadTokenError:
        return render_template('releasenotes.html', oauth_url=OAUTH_URL)
    return render_template('releasenotes.html', oauth_url=OAUTH_URL)
# gonna have a history of release nots so version is required, it also makes it easier to just open old release notes

@app.route('/spacecases/aboutthedevs')
def devsinfo():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('devinfo.html', current_user=current_user)
    except BadTokenError:
        return render_template('devinfo.html', oauth_url=OAUTH_URL)
    return render_template('devinfo.html', oauth_url=OAUTH_URL)

@app.route('/spacecases/test')
def test():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('test.html', current_user=current_user)
    except BadTokenError:
        return render_template('test.html', oauth_url=OAUTH_URL)
    return render_template('test.html', oauth_url=OAUTH_URL)



