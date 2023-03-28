from flask import render_template, request, Blueprint, session
from zenora import APIClient
from zenora.exceptions import BadTokenError
from webstart.config import _blueprint_config_data

errors = Blueprint('errors', __name__)

#|--ERROR HANDLING--|#
@errors.app_errorhandler(400)
def page_not_found(e):
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('400.html', current_user=current_user)
    except BadTokenError:
        return render_template('400.html', oauth_url=_blueprint_config_data.OAUTH_URL), 400
    return render_template('400.html', oauth_url=_blueprint_config_data.OAUTH_URL), 400


@errors.app_errorhandler(401)
def page_not_found(e):
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('401.html', current_user=current_user)
    except BadTokenError:
        return render_template('401.html', oauth_url=_blueprint_config_data.OAUTH_URL), 401
    return render_template('401.html', oauth_url=_blueprint_config_data.OAUTH_URL), 401


@errors.app_errorhandler(403)
def page_not_found(e):
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('403.html', current_user=current_user)
    except BadTokenError:
        return render_template('403.html', oauth_url=_blueprint_config_data.OAUTH_URL), 403
    return render_template('403.html', oauth_url=_blueprint_config_data.OAUTH_URL), 403


@errors.app_errorhandler(404)
def page_not_found(e):
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('404.html', current_user=current_user)
    except BadTokenError:
        return render_template('404.html', oauth_url=_blueprint_config_data.OAUTH_URL), 404
    return render_template('404.html', oauth_url=_blueprint_config_data.OAUTH_URL), 404


@errors.app_errorhandler(500)
def page_not_found(e):
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('500.html', current_user=current_user)
    except BadTokenError:
        return render_template('500.html', oauth_url=_blueprint_config_data.OAUTH_URL), 500
    return render_template('500.html', oauth_url=_blueprint_config_data.OAUTH_URL), 500

