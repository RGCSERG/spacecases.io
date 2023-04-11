from flask import render_template, request, Blueprint, session, redirect
from zenora import APIClient
from webstart.config import _blueprint_config_data
from zenora.exceptions import BadTokenError
from webstart import db

users = Blueprint('users', __name__)

@users.route('/profile')
def profile():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            if db.user_data.find_one({"_id": current_user.id}) is not None:  
                return render_template('profile.html', current_user=current_user, authenticated_user=True)
            return render_template('profile.html', current_user=current_user)
    except BadTokenError:
        return render_template('profile.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return redirect(_blueprint_config_data.OAUTH_URL)


@users.route('/logout')
def logout():
    session.clear()
    return redirect("/")