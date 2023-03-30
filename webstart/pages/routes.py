from flask import render_template, request, Blueprint, session
from zenora import APIClient
from zenora.exceptions import BadTokenError
from webstart.config import _blueprint_config_data
from webstart import db

pages = Blueprint('pages', __name__)



@pages.route('/socials')
def socials():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            if db.user_data.find_one({"_id": current_user.id}) is not None:  
                return render_template('socials.html', current_user=current_user, authenticated_user=True)
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
            if db.user_data.find_one({"_id": current_user.id}) is not None:  
                return render_template('premium.html', current_user=current_user, authenticated_user=True)
            return render_template('premium.html', current_user=current_user)
    except BadTokenError:
        return render_template('premium.html', oauth_url=_blueprint_config_data.OAUTH_URL)
    return render_template('premium.html', oauth_url=_blueprint_config_data.OAUTH_URL)



@pages.route('/patch_notes/version=<string:version>')
def patch_notes(version):
    if version == 'latest-release':
        # patch_notes = db.patch_notes.find_one({'$query':{},'$orderby':{'_id':-1}})
        patch_notes = [patch_note for patch_note in db.patch_notes.find().sort('Version',-1).limit(5)]
    elif isinstance(version, int):
        patch_notes = [db.patch_notes.find_one({'Version': version})]
    else:
        raise(404)
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            if db.user_data.find_one({"_id": current_user.id}) is not None:  
                return render_template('patch_notes.html', current_user=current_user, patch_notes=patch_notes, authenticated_user=True)
            return render_template('patch_notes.html', current_user=current_user, patch_notes=patch_notes)
    except BadTokenError:
        return render_template('patch_notes.html', oauth_url=_blueprint_config_data.OAUTH_URL, patch_notes=patch_notes)
    return render_template('patch_notes.html', oauth_url=_blueprint_config_data.OAUTH_URL, patch_notes=patch_notes)
# gonna have a history of release nots so version is required, it also makes it easier to just open old release notes

@pages.route('/aboutthedevs')
def devsinfo():
    try:
        if 'token' in session:
            bearer_client = APIClient(session.get('token'), bearer=True)
            current_user = bearer_client.users.get_current_user()
            if db.user_data.find_one({"_id": current_user.id}) is not None:  
                return render_template('devinfo.html', current_user=current_user, authenticated_user=True)
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
            if db.user_data.find_one({"_id": current_user.id}) is not None:  
                return render_template('test.html', current_user=current_user, authenticated_user=True)
            return render_template('test.html', current_user=current_user)
    except BadTokenError:
        return render_template('test.html')
    return render_template('test.html')