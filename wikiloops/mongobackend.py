from pymongo.connection import Connection
MONGO_LOCATION = 'locahost'
DB_NAME = 'wikiloops'
COLLECTION_NAME = 'pages'


class LinkAdder(object):
    def __init__(self, host=MONGO_LOCATION, db=DB_NAME, coll=COLLECTION_NAME):
        self.collection = Connection('localhost')['wikiloops']['pages']
        self.counter = 0

    def make_links(self, parent, links, name='forward-links'):
        obj = dict(page=parent)
        obj[name]=links
        self.collection.save(obj)
        self.counter += 1
        if self.counter%50 == 0:
            print "saved %d pages" %self.counter
