import re
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

from mongobackend import LinkAdder

CAMEL_RE = re.compile("([a-z])([A-Z])")
LINK_RE = re.compile(r'\[\[([\w ()]+)(?:\|.*?)?\]\]')
REDIRECT_RE = re.compile(r'^#REDIRECT')

def parsewiki(filename):
    parser = make_parser()
    parser.setContentHandler(WikiHandler())
    parser.parse(open(filename, 'r'))


class WikiHandler(ContentHandler):
    def __init__(self):
        self.linkadder = LinkAdder()
        self.in_text = False
        self.in_title = False
        self.title = ''
        self.text = ''

    def startElement(self, name, attrs):
        if name == 'title':
            self.in_title = True
            self.title = ''
        elif name == 'text':
            self.text = ''
            self.in_text = True

    def characters(self, chars):
        """ it would be better to just process these but
            I think that can break up information  """
        if self.in_title:
            self.title += chars
        elif self.in_text:
            self.text += chars

    def endElement(self, name):
        if name == 'title':
            self.title = CAMEL_RE.sub("\g<1> \g<2>",self.title).lower()
            self.in_title = False
        if name == 'text':
            self.in_text = False
            self.find_links(self.title, self.text)

    def find_links(self, title, text):
        if REDIRECT_RE.match(text):
            redirect = True
        else:
            redirect = False
        self.linkadder.make_links(title, [m.groups()[0].lower() for m in LINK_RE.finditer(text)], redirect=redirect)
