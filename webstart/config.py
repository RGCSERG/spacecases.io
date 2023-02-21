import os
from urllib import parse

#try read tokens from text file, if it fails use environment variables

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
OAUTH_URL = f'https://discord.com/api/oauth2/authorize?client_id=1025496377939197972&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify'
INVITE_URL = 'https://discord.com/api/oauth2/authorize?client_id=1025496377939197972&permissions=395136993280&scope=bot'