from pymongo import MongoClient
from bson.objectid import ObjectId

class AACShelter(object):
    def __init__(self):
        # initializing mongo client as aacuser
        self.client = MongoClient('mongodb://%s:%s@localhost:48927' % ('admin','admin'))
        self.database = self.client['project']
        
    # method to insert new documents into the collection
    def create(self, doc = None):
        #doc must be a dictionary
        if doc is None:
            raise Exception("No document provided.")
            return False
        else:
            # return true if successful, false if not
            self.database.animals.insert(doc)
            return True
        
    # method to query the database
    def query(self, q = {}):
        if len(q) == 0:
            # find all (no query)
            data = self.database.animals.find({},{"_id":False})
        else:
            # find documents that match query
            data = self.database.animals.find(q,{"_id":False})
        return data