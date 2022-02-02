''' Cats controller '''
from werkzeug.exceptions import NotFound, InternalServerError
from pymongo import MongoClient
import random
import string

client = MongoClient('localhost', 27017)

col = client.mydb.urls
col.drop()

urls = [
    {'long_url': 'http://www.bbc.co.uk', 'short_url': 'beeb'}
]
    
col.insert_many(urls)

def getShortUrl():
    url = string.ascii_lowercase + string.digits
    return ''.join(random.choice(url) for i in range(6))

def get_all():
    return {'entries': list(col.find({}, {'_id': 0}))}, 200

def create_short_url(req):
    shortUrl = getShortUrl()
    res = col.insert_one({'long_url': req['long_url'], 'short_url': shortUrl})
    if res.inserted_id:
        return {'short_url': shortUrl }, 200
    else:
        raise InternalServerError("Could not create entry")


def find_by_short_url(short_url):
    res = col.find_one({'short_url': short_url}, {'_id': 0, 'long_url': 1})
    if res is None:
        raise NotFound(f"We don't have a short url for this url: {short_url}!")
    else:
        return res['long_url']