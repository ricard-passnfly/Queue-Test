import flask

api_blueprint = flask.Blueprint('API', __name__, url_prefix='/api')

import pymongo
from bson import json_util as j
from bson import ObjectId

connection = pymongo.MongoClient()
db = connection.users
collection = db.tickets


######################
# AUXILIAR FUNCTIONS #
######################


def delete_ticket(ticket_id):
    x = None
    try:
        x = collection.remove({'_id': ObjectId(ticket_id)})
    except Exception as e:
        print(e)

    return x

def exportDB(exportroute):
    try:
        with open(exportroute, 'w') as f:
            data = collection.find()
            dump = j.dumps([entry for entry in data], sort_keys=False, indent=4, default=j.default)
            f.write(dump)
    except Exception as e:
        print(e)



############
# BINDINGS #
############

@api_blueprint.route('/test/')
def test_binding():
    return flask.jsonify('Blueprint loaded correctly')

# TODO: Make sure bindings are similar to current ones
# Does it make sense to constantly refresh the DB?
@api_blueprint.route('/getTicket/')
@api_blueprint.route('/getTicket/<numTickets>')
def get_tickets(numTickets=1):
    # Current API seems to return an array of tickets in json
    # Right now we just return a single item

    result = None

    # In case of loading from file
    if numTickets == 1:
        result = collection.find_one()
        delete_ticket(result.get('_id'))
    else:
        result = []
        for entry in collection.find()[:numTickets]:
            result.append(entry)
            # We delete the ticket now or later?
            delete_ticket(entry.get('_id'))

    return j.dumps(result)
