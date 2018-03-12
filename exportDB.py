from pymongo import MongoClient
from bson import json_util as j



if __name__ == '__main__':
    print("Importing a Json into mongo")

    # Get the current JSON
    with open('tickets_pending.json') as f:
        json_file = j.loads(f.read())
    connection = MongoClient()
    db = connection.users
    collection = db.tickets
    data = collection.find()

    # Export DB json to file
    with open('export.json', 'w') as f:
        dump = j.dumps([entry for entry in data], sort_keys=False, indent=4, default=j.default)
        f.write(dump)

    print ("Done!")