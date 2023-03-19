from os import environ
import pymongo
import json
import certifi
from pymongo.collection import Collection
from timeit import default_timer as timer
from datetime import timedelta


NO_PRICE_FOUND = 300000

user_data: Collection  # user data - mongodb
trade_requests: Collection  # trade requests - mongodb
guild_data: Collection  # guild data - mongodb
skin_data_collection:Collection # skin data - mongodb

mongo_client: pymongo.MongoClient

leaderboard = []  # user leaderboard
rooms = {}
wordle_games = {}
skin_data = {}
skin_data_hl = {}  # SKIN DATA for higher lower game - does not include knives, glov
containers = {}
word_list = []



# update the leaderboard
def get_leaderboard():
  global leaderboard

  start = timer()
  all_users_data = user_data.find({}).batch_size(4)

  leaderboard = sorted([(user_data["_id"], sum([skin_data["skins"][item["name"]]["price"] for item in user_data["inventory"]])) for user_data in all_users_data], key=lambda x: x[1], reverse=True)
  end = timer()

  print(f"Generated leaderboard in {timedelta(seconds=end-start)}")


def init():

    global user_data, trade_requests, mongo_client, skin_data, skin_data_hl, containers, guild_data, word_list

    # try read mongodb database password from database_pass.txt, if fails read from environment variable
    try:
        # read local bot_info
        f = open("database_pass.txt", "r")
        PASS = f.read()
    except:
        # read password from environment variable
        PASS = environ["MONGO_DB_PASS"]

    # setup mongodb database
    mongo_url = f"mongodb+srv://admin:{PASS}@csgo-case-bot.odtd2un.mongodb.net/?retryWrites=true&w=majority"
    mongo_client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

    print("Connected to MongoDB database!")

    # load the csgo bot database
    db = mongo_client['csgo-case-bot']

    # user data collection
    user_data = db["user-data"]
    trade_requests = db["trade-requests"]
    guild_data = db["guild-data"]
    skin_data_collection = db["skin-data"] # load skin data collection ( 2files )
    skin_data = skin_data_collection.find_one({"_id": "skin-data"}) # load skin data file


    print("Loaded user data + skin data")



