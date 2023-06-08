# https://realpython.com/introduction-to-mongodb-and-python/#using-mongodb-with-python-and-mongoengine


from pymongo import MongoClient

connection_string = 'mongodb://root:p4ssw0rd@localhost:27017/?retryWrites=true&w=majority'

client = MongoClient(connection_string)

db = client.users

collection = db.users

user = {
    'name': 'peter',
    'password_hash': 'xxxx',
    'secrets': [
        {'name': 'password', 'content': 'p4ssw0rd'},
        {'name': 'pin', 'content': '1234'}
    ]
}

result = collection.insert_one(user)
print(result)

result = collection.find().next()
print(result)
