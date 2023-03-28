from flask import render_template, request, Blueprint, session, redirect
from zenora import APIClient
from webstart.config import _blueprint_config_data

users = Blueprint('users', __name__)

@users.route('/profile')
def profile():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('profile.html', current_user=current_user)

    return render_template('profile.html', oauth_url=_blueprint_config_data.OAUTH_URL)

@users.route('/logout')
def logout():
    session.clear()
    return redirect("/")