''' Cats controller '''
from werkzeug.exceptions import BadRequest, NotFound
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

col = client.mydb.cats
col.drop()

cats = [
    {'name': 'Zelda', 'age': 3},
    {'name': 'Tigerlily', 'age': 9},
    {'name': 'Salem', 'age': 500}
]
    
col.insert_many(cats)

def index(req):
    return {'entries': list(col.find({}, {'_id': 0}))}, 200

def show(req, cat_name):
    cat = col.find_one({'name': cat_name}, {'_id': 0})
    if cat:
        return cat, 200
    else:
        raise BadRequest(f"We don't have that cat with name {cat_name}!")

def create(req):
    res = col.insert_one(req.get_json())
    if res.inserted_id:
        return {'new entry': str(res.inserted_id)}, 200
    else:
        raise NotFound("Could not create entry")

def update(req, cat_name):
    res = col.update_one({'name': cat_name}, {'$set': req.get_json()})
    if res.acknowledged:
        return {'m': f"{cat_name} updated"}, 200
    else:
        raise NotFound("Could not update entry")

def destroy(req, cat_name):
    res = col.delete_one({'name': cat_name})
    if res.deleted_count > 0:
        return {'m': f'{cat_name} deleted'}, 204
    else:
        raise NotFound(f'Could not delete {cat_name} does not exist')

def find_by_uid(uid):
    try:
        return next(cat for cat in cats if cat['id'] == uid)
    except:
        raise BadRequest(f"We don't have that cat with id {uid}!")