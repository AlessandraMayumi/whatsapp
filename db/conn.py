import os
import logging

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')
log = logging.getLogger('conn')


class DatabaseService:

    def __init__(self):
        self.client = None
        self.db = None
        self.col = None

    def __connect(self):
        if not self.client:
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
        log.info(chat)
        return self.col.insert_many(chat)

    def find_one(self, filter: dict):
        self.__connect()
        return self.col.find_one(filter=filter)

    def update_one(self, from_, header, body, status):
        self.__connect()
        status += 1
        return self.col.update_one({"from": from_}, {"$set": {header: body, "status": status}})
