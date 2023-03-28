from flask import render_template, request, Blueprint, session
from zenora import APIClient
from webstart.config import _blueprint_config_data
from webstart import Client, db
from webstart.calculations import updateLD, iscasesin, permissions
from webstart.database_commands import get_leaderboard

bot_management = Blueprint('bot_management', __name__)

@bot_management.route('/leaderboard')
def leaderboard():
    Leaderboard, status = updateLD(Client, get_leaderboard, db)
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        guilds = iscasesin(bearer_client.users.get_my_guilds(), Client.users.get_my_guilds())
        return render_template('leaderboard.html',oauth_url=_blueprint_config_data.OAUTH_URL,Leaderboard=Leaderboard,current_user=current_user,guilds=guilds,str=str,len=len,iterate=status) # remove [:10] when updateLD is fixed and not using setlist
    return render_template('leaderboard.html',oauth_url=_blueprint_config_data.OAUTH_URL,Leaderboard=Leaderboard,len=len,iterate=status) # remove [:10] when updateLD is fixed and not using setlist


@bot_management.route('/invite_server')
def invite_server():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        guilds = permissions(bearer_client.users.get_my_guilds())
        return render_template('invite_Server.html', current_user=current_user, guilds=guilds, invite_url=_blueprint_config_data.INVITE_URL, str=str)
    return render_template('invite_server.html', oauth_url=_blueprint_config_data.OAUTH_URL, invite_url=_blueprint_config_data.INVITE_URL)