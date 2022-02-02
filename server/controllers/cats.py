''' Cats controller '''
from werkzeug.exceptions import BadRequest, NotFound
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

col = client.mydb.urls
col.drop()

urls = [
    {'longUrl': 'www.bbc.co.uk', 'shortUrl': 'beeb'}
]
    
col.insert_many(urls)

def index(req):
    return {'entries': list(col.find({}, {'_id': 0}))}, 200

def show(req, long_url):
    url = col.find_one({'longUrl': long_url})
    if url:
        return url, 200
    else:
        create_short_url(req, long_url)

def create_short_url(long_url):
    # complete the logic to generate short url
    shortUrl = ''
    res = col.insert_one({'longUrl': long_url, 'shortUrl': shortUrl})
    if res.inserted_id:
        return {'new entry': str(res.inserted_id)}, 200
    else:
        raise NotFound("Could not create entry")

def find_by_long_url(long_url):
    try:
        return next(url for url in urls if urls['longUrl'] == long_url)
    except:
        raise BadRequest(f"We don't have a short url for this url: {long_url}!")