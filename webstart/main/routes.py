from flask import render_template, request, Blueprint, session
from zenora import APIClient
from webstart.config import _blueprint_config_data
from zenora.exceptions import BadTokenError
#instead of using discord ouath to return bot info about user return by batabse ID to save Client acess rate
#release notes page
#Devs page
#second db or rework on leaderboard + remember cookies attr for users + server leaderboards rework
#patreon
#add if statement for invite server
#can remove cookies ask for now
#check if current_user in session works -- can confirm you can't add current_user to json file as it is a class

main = Blueprint('main', __name__)

@main.route('/')
# def check_for_user():
#     return redirect('/get')
@main.route('/home')
def home():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            return render_template('home.html', current_user=current_user)
    except BadTokenError:
        return render_template('home.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return render_template('home.html', oauth_url=_blueprint_config_data.OAUTH_URL)