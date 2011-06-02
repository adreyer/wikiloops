from pymongo.connection import Connection
MONGO_LOCATION = 'locahost'
DB_NAME = 'wikiloops'
COLLECTION_NAME = 'pages'


class LinkAdder(object):
    def __init__(self, host=MONGO_LOCATION, db=DB_NAME):
        self.conn = Connection('localhost')[db]
        self.pages = self.conn['pages']
        self.redirs = self.conn.redirects
        self.counter = 0

    def make_links(self, parent, links, name='links', redirect=False):
        obj = dict(page=parent)
        print parent
        # fixing redirects is a one time thing so only save it if they exist
        if redirect:
            obj['redirect'] = links[0]
            self.redirs.save(obj)
        else:
            # setify everything here, maybe we should do it in mongo
            linkset = set(links)
            uniquelinks = len(linkset)
            index = 0
            while len(links) > uniquelinks:
                try:
                    linkset.remove(links[index])
                except KeyError:
                    links.pop(index)
                else:
                    index += 1
            # now save the links                
            obj[name]=links
            self.pages.save(obj)
        self.counter += 1
        if self.counter%5 == 0:
            print "saved %d pages" %self.counter
