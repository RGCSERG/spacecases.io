from flask import render_template, request, Blueprint, session, make_response, redirect
from zenora import APIClient
from webstart.config import _blueprint_config_data
from webstart import Client

oauth2 = Blueprint("oauth2", __name__)


@oauth2.route("/oauth/callback")
def callback():
    code = request.args["code"]
    resp = Client.oauth.get_access_token(code, _blueprint_config_data.REDIRECT_URI)

    # Authentication successful - store tokens in session
    session["token"] = resp.access_token
    session["refresh_token"] = resp.refresh_token
    if request.cookies.get("redirect_before_oauth2") is not None:
        return redirect(f"{request.cookies.get('redirect_before_oauth2')}")
    return redirect("/home")
