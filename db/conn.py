import os
import logging

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')


class DatabaseService:

    def __init__(self):
        self.client = None
        self.db = None
        self.col = None

    def __connect(self):
        user = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASS")
        url = f"mongodb+srv://{user}:{password}@cluster0.4mmpg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.client = MongoClient(url)
        self.client.server_info()
        self.db: Database = self.client['myFirstDatabase']
        self.col: Collection = self.db['chats']

    def insert(self, chat=None):
        self.__connect()
        if chat is None:
            chat = [{'insert': "failed"}]
        return self.col.insert_many(chat)


db = DatabaseService()
db.insert()
