# CSC 242-503
# Lab 8 template


from html.parser import HTMLParser
from urllib.request import urlopen

# Question 1
class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title = ""
        self.bool = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.bool = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.bool = False

    def handle_data(self, data):
        if self.bool == True:
            self.title += data.strip()

    def getTitle(self):
        return self.title

# Provided for testing only
# Do not modify
def testTParser(url):
    'Test the TitleParser class'
    content = urlopen(url).read().decode()
    tParser = TitleParser()
    tParser.feed(content)
    return tParser.getTitle()

# Question 2
class HeaderParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.boole = False
        self.headings = []

    def handle_starttag(self, tag, attrs):
        if "h" in tag and tag not in ['head', 'html']: 
            self.boole = True

    def handle_endtag(self, tag):
        if "h" in tag and tag not in ['head', 'html']:
            self.boole = False

    def handle_data(self, data):
        if self.boole == True:
            self.headings.append(str(data.strip()))

    def getHeadings(self):
        return self.headings

# For testing purposes only
# Do not modify
def testHParser(url):
    'Test the HeaderParser class'
    content = urlopen(url).read().decode()
    hParser = HeaderParser()
    hParser.feed(content)
    return hParser.getHeadings()
