from os import environ
import pymongo
import json
import certifi
from pymongo.collection import Collection
from timeit import default_timer as timer

user_data: Collection # user data - mongodb

def init():

  global user_data, mongo_client
  #try read mongodb database password from database_pass.txt, if fails read from environment variable
  try:
      #read local bot_info
      f = open("database_pass.txt", "r")
      PASS = f.read()
  except:
      #read password from environment variable
      PASS = environ["MONGO_DB_PASS"]

  #setup mongodb database
  mongo_url = f"mongodb+srv://admin:{PASS}@csgo-case-bot.odtd2un.mongodb.net/?retryWrites=true&w=majority"
  mongo_client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

  print("Connected to MongoDB database!")

  #load the csgo bot database
  db = mongo_client['csgo-case-bot']

  #user data collection
  user_data = db["user-data"]