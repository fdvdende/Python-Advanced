import pymongo
import sys


class Database:

    connection_string = 'mongodb://root:p4ssw0rd@localhost:27017/?retryWrites=true&w=majority'

    def __init__(self):
        try:
            self.client = pymongo.MongoClient(self.connection_string)

        except pymongo.errors.ConfigurationError:
            print("An Invalid URI host error was received.")
            sys.exit(1)

        # use a database named "myDatabase"
        self.db = self.client.myDatabase

        # use a collection named "recipes"
        self.collection = self.db['secrets']
