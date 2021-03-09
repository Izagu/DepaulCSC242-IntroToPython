# CSC 242-503
# Lab 9 template
# Yanacey

import os
from html.parser import HTMLParser
from urllib.request import urlopen

# The first function must be recursive and may not use global variables.
# You may not define any helper functions or modify the header of the
# function.

# Question 1
def hasPyDir(path):
    for item in os.listdir(path):
        if item[0] != '.':
            n = os.path.join(path, item)
            if os.path.isfile(n):
                if item.lower().endswith('.py'):
                    return True
            
            elif os.path.isdir(n):
                count = hasPyDir(n)
                if count == True:
                    return count

    return False
# Question 2
class ListCounter(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.count = 0
        self.counts = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "ol" or tag.lower() =="ul":
            self.count += 1
            if self.count == 1:
                self.counts +=1
        
    def handle_endtag(self, tag):
        if tag.lower() == "ol" or tag.lower() =="ul":
            self.count -= 1
    
    def getCount(self):
        return self.counts
    
# For reference only -- do not change
def testParser(url):
    content = urlopen(url).read().decode()
    parser = ListCounter()
    parser.feed(content)
    return parser.getCount()
