import redis

# subclass?
class LinkAdder(object):
    def __init__(self, host='localhost'):
        self.conn = redis.Redis(host)

    def make_links(self, parent, links, name="flink"):
        for link, i in zip(links, range(len(links))):
            self.conn.zadd("%s:%s"%(parent,name), link, i)
