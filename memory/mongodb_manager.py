from pymongo import MongoClient
import os
class MongodbManager:
      def __init__(self,db_name="assitant_db"):
            self.client=MongoClient(os.getenv("MONGO_URI"))
            self.db=self.client[db_name]

      def get_collection(self,collection_name):
            return self.db[collection_name]