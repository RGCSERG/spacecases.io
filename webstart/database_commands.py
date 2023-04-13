import os
import pymongo
import certifi
from pymongo.collection import Collection
from timeit import default_timer as timer
from datetime import timedelta, datetime

try:
    from leaderboard import Leaderboard
except:
    Leaderboard = ['404 NO LEADERBOARD FOUND']
try:
    from leaderboard import unfiltered_Leaderboard
except:
    unfiltered_Leaderboard = ['404 NO LEADERBOARD FOUND']

# MongoDB collections
user_data: Collection
trade_requests: Collection
guild_data: Collection
skin_data: Collection
patch_notes: Collection

mongo_client: pymongo.MongoClient

leaderboard = []
unfiltered_leaderboard = []
skin_data = {}


# update the leaderboard
def get_leaderboard():
    global leaderboard, unfiltered_leaderboard
    if (datetime.now()- datetime.fromtimestamp(os.path.getmtime('leaderboard.py'))).seconds < 86400: #86400 is one day in seconds so updates leaderboard accordingly
        if Leaderboard == []:
            leaderboard = ['404 NO LEADERBOARD FOUND']
        leaderboard = Leaderboard
        if unfiltered_Leaderboard == []:
            unfiltered_leaderboard = ['404 NO LEADERBOARD FOUND']
        unfiltered_leaderboard = unfiltered_Leaderboard
        print('Leaderboard retrived')
        return

    start = timer()
    all_users_data = user_data.find({}).batch_size(4)

    leaderboard = sorted(
        [
            (
                user_data["_id"],
                sum(
                    [
                        skin_data["skins"][item["name"]]["price"]
                        for item in user_data["inventory"]
                    ]
                ),
                user_data["lang"],
            )
            for user_data in all_users_data
        ],
        key=lambda x: x[1],
        reverse=True,
    )
    end = timer()
    print(f"Generated leaderboard in {timedelta(seconds=end-start)}")


def init():
    global user_data, trade_requests, mongo_client, skin_data, guild_data, patch_notes

    # try read mongodb database password from database_pass.txt, if fails read from environment variable
    try:
        # read local bot_info
        f = open("database_pass.txt", "r")
        PASS = f.read()
    except:
        # read password from environment variable
        PASS = os.environ["MONGO_DB_PASS"]

    # connect to MongoDB
    mongo_url = f"mongodb+srv://admin:{PASS}@csgo-case-bot.odtd2un.mongodb.net/?retryWrites=true&w=majority"
    mongo_client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

    print("Connected to MongoDB database!")

    # load the csgo bot database
    db = mongo_client["csgo-case-bot"]

    # load all collections from the database
    user_data = db["user-data"]
    trade_requests = db["trade-requests"]
    guild_data = db["guild-data"]
    patch_notes = db["patch-notes"]
    skin_data = db["skin-data"]

    # load our skin data
    skin_data = skin_data.find_one({"_id": "skin-data"})

    print("Loaded user data + skin data")
