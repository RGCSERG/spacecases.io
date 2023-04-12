from flask import render_template, request, Blueprint, session, redirect, make_response
from zenora import APIClient
from webstart.config import _blueprint_config_data
from zenora.exceptions import BadTokenError
from webstart import db
from webstart.calculations import get_user_inv
from datetime import datetime

users = Blueprint('users', __name__)

@users.route('/profile')
def profile():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            resp = make_response(redirect('/home'))
            if db.user_data.find_one({"_id": current_user.id}) is not None:
                user_data = get_user_inv(db,datetime, current_user.id)
                resp = make_response(render_template('profile.html', current_user=current_user, user_data=user_data, authenticated_user=True))
                resp.delete_cookie('redirect_before_oauth2') 
                return resp
            resp.delete_cookie('redirect_before_oauth2')
            return resp
    except BadTokenError:
        return render_template('profile.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    resp = make_response(redirect(_blueprint_config_data.OAUTH_URL))
    resp.set_cookie('redirect_before_oauth2', request.url)
    return resp


@users.route('/logout')
def logout():
    session.clear()
    resp = make_response(redirect("/"))
    resp.delete_cookie('tokens')
    return resp