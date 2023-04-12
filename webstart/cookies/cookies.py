from flask import render_template, request, Blueprint, session, make_response, redirect
from zenora import APIClient
from webstart.config import _blueprint_config_data
from webstart import Client

cookies = Blueprint('cookies', __name__)

# @cookies.route('/cookies_policy:accept&deny/<int:userid>', methods= ['POST', 'GET'])
# def cookies_policy(userid):
#     if request.method == 'POST':
#         acceptdeny = request.form['cookies_policy']
#         return
#     return
#fix db issues so can add a data check then make it into an list of objects etc yk what im getting at

# @app.route('cookies/user:tokens/get')
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
#             return redirect('/home')
#         try:
#             session['token'] = access_token
#             bearer_client = APIClient(session.get('token'), bearer=True)#
#         except BadTokenError:
#             return redirect('/home')