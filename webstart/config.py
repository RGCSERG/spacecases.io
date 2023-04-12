import os
from urllib import parse

#try read tokens from text file, if it fails use environment variables
#"".join(secrets.choice(string.ascii_letters + string.punctuation + string.digits) for i in range(200))
class Config_data: # config data for the app
    try:
        with open("secret_key.txt", "r") as file:
            SECRET_KEY = file.read()
    except FileNotFoundError:
        SECRET_KEY = os.environ["SECRET_KEY"] # sets scret key for flask context
        SESSION_PERMANENT = True # i am certain this does nothing
        SESSION_COOKIE_DOMAIN = 'http://localhost:5000/oauth/callback' # honestly have no idea why this is nessasry but it works so yeah

class _blueprint_config_data: # blueprint condig data for general use in routes
    try:
        with open("bot_token.txt", "r") as file:
            TOKEN = file.read()
    except FileNotFoundError:
        TOKEN = os.environ["BOT_TOKEN"]
    try:
        with open("client_secret.txt", "r") as file:
            CLIENT_SECRET = file.read()
    except FileNotFoundError:
        CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    REDIRECT_URI = 'http://localhost:5000/oauth/callback'
    OAUTH_URL = f'https://discord.com/api/oauth2/authorize?client_id=1025496377939197972&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify%20email%20guilds%20applications.commands.permissions.update'
    INVITE_URL = 'https://discord.com/api/oauth2/authorize?client_id=1025496377939197972&permissions=395136993280&guild_id=1050490944232890389&scope=bot'