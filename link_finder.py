# This module defines LinkFinder class to find all the links in HTML code
from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__() # access HTMLParser
        self.base_url = base_url # homepage link
        self.page_url = page_url # current page link
        self.links = set() # containing all the crawling link
    
    def handle_starttag(self, tag, attrs):
        # this method is called whenever encounter a start tag
        # tag holds start tag name
        if tag == 'a':
            # attrs holds a list of elements, which each element is a 2-elements tuple (attribute name and value)
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value) # absolute file path
                    self.links.add(url)

    def page_links(self):
        # returns the crawling links
        return self.links
    
    def error(self, message):
        pass


# finder = LinkFinder()
# finder.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')
