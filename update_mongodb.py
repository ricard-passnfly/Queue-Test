import celery
from celery.schedules import crontab
import requests

from pymongo import MongoClient
from bson import json_util

app = celery.Celery()


@app.on_after_configure.connect
def setup_task():
    pass


@app.task
def update_mongodb():
    # Get the current JSON
    json_file = None

    # FROM FILE
    # with open('tickets_pending.json') as f:
    #     json_file = json_util.loads(f.read())
    # FROM DB
    statuses = 'pending'
    x = requests.get('http://server.passnfly.com/dcip/ticketsSearch/now/{}'.format(statuses))

    # Insert into Mongo
    connection = MongoClient()
    db = connection.users
    collection = db.tickets
    res = collection.drop()
    idx = collection.insert_many(json_file)


if __name__ == '__main__':
    pass

