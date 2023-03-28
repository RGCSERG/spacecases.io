from flask import render_template, request, Blueprint, session, make_response, redirect
from zenora import APIClient
from webstart.config import _blueprint_config_data
from webstart import Client


oauth2 = Blueprint('oauth2', __name__)


@oauth2.route('/oauth/callback')
def callback():
    code = request.args['code']
    resp = Client.oauth.get_access_token(code,_blueprint_config_data.REDIRECT_URI)
    session['token'] = resp.access_token
    session['refresh_token'] = resp.refresh_token
    session.permanent = True
    # cookie_set = make_response(redirect('/spacecases/home'))
    # cookie_set.set_cookie('tokens', resp.access_token + ':' + resp.refresh_token + ':' + resp.scope  + ':' + resp.token_type)

    return redirect('/home')

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