from flask import render_template, request, Blueprint, session
from zenora import APIClient
from zenora.exceptions import BadTokenError
from webstart.config import _blueprint_config_data

pages = Blueprint('pages', __name__)



@pages.route('/socials')
def socials():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('socials.html', current_user=current_user)
    except BadTokenError:
        return render_template('socials.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return render_template('socials.html', oauth_url=_blueprint_config_data.OAUTH_URL)


@pages.route('/premium')
def premium():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('premium.html', current_user=current_user)
    except BadTokenError:
        return render_template('premium.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return render_template('premium.html', oauth_url=_blueprint_config_data.OAUTH_URL)



@pages.route('/release_notes/version=<string:version>')
def releasenotes(version):
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('release_notes.html', current_user=current_user, version=version)
    except BadTokenError:
        return render_template('release_notes.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return render_template('release_notes.html', oauth_url=_blueprint_config_data.OAUTH_URL)
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
        return render_template('test.html')
    return render_template('test.html')