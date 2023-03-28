from flask import render_template, request, Blueprint, session
from zenora import APIClient
from zenora.exceptions import BadTokenError
from webstart.config import _blueprint_config_data

pages = Blueprint('pages', __name__)



@pages.route('/socials')
def socials():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('profile.html', current_user=current_user)

    return render_template('profile.html', oauth_url=_blueprint_config_data.OAUTH_URL)

@pages.route('/premium')
def premium():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('profile.html', current_user=current_user)

    return render_template('profile.html', oauth_url=_blueprint_config_data.OAUTH_URL)


@pages.route('/release_notes/<version>')
def releasenotes(version):
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('releasenotes.html', current_user=current_user)
    except BadTokenError:
        return render_template('releasenotes.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return render_template('releasenotes.html', oauth_url=_blueprint_config_data.OAUTH_URL)
# gonna have a history of release nots so version is required, it also makes it easier to just open old release notes

@pages.route('/aboutthedevs')
def devsinfo():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('devinfo.html', current_user=current_user)
    except BadTokenError:
        return render_template('devinfo.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return render_template('devinfo.html', oauth_url=_blueprint_config_data.OAUTH_URL)

@pages.route('/test')
def test():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('test.html', current_user=current_user)
    except BadTokenError:
        return render_template('test.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return render_template('test.html', oauth_url=_blueprint_config_data.OAUTH_URL)