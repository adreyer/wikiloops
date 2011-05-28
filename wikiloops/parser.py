from xml.sax.handler import ContentHandler

class WikiHandler(ContentHandler):
    def __init__(self):
        self.in_text = False
        self.title = ''
        self.text = ''

    def startElement(self, name, attrs):
        if name = 'title'
            self.in_title = True
            self.curr_title = ''
        elif name = 'text':
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
        if name = 'title'
            self.title = clean_title(self.title)
        if name = 'text':
            make_links(self.title, self.text)

upre = re.compile('[A-Z]')

def clean_title(title):
    """ turns camel case to lowercase split """


linkre = re.compile(r'\[\[([\w ()]+)\|.*?\]\]')
def find_links(title, text):
    for match in linkre.finditer(text):
        make_link(title, match.groups()[0])    
