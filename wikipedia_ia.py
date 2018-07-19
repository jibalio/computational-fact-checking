"""
Computational Fact Checking
Alfafara, Lean Raphael
Ibalio, Jan Leryc
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
import wikipedia
import re
import requests
import urllib.request
import json
import wikipedia
import math

TOKEN = r"1532025693|20fdd78accfc72489ad261e63c2b3067"
DEBUG = True
DEBUG_PROMPT = ">>> DEBUG:  "

class Path:

    _degrees = []
    _truth_value = None

    def __init__(self, a1, a2, preload_degrees=False):

        dprint("Creating Path object [ %s => %s ]." % (a1.title, a2.title))

        # Get the list of nodes traversed by the path.
        self.nodes = [Page(x.replace("_", " ")) for x in get_path(a1.title.replace(" ", "+"), a2.title.replace(" ", "+"))][1:]
        dprint("Successfully detected path %s" % (self.nodes))

        # Load the degrees. Set preload_degrees to False to avoid long waiting
        # times when instantiating a path.
        if preload_degrees:
            self._degrees = [len(x.backlinks) for x in self.nodes]
        
    
    @property
    def degrees(self):
        if not self._degrees:
            self._degrees = [len(x.backlinks) for x in self.nodes]
        return self._degrees

    @property
    def truthvalue(self):
        if not self._truth_value:
            cnt = -1
            added_weight = 0
            for x in self.degrees:
                cnt+=1
                if cnt==0:      # ignore first node (this always defaults to 1)
                    continue
                added_weight+=math.log(x)
                dprint("itr:%s; deg:%s; log:%s; acc:%s" % (cnt,x,math.log(x), added_weight))
            self._truth_value =  (1/(1+added_weight))
        return self._truth_value

        
        






        


"""
This class extends wikipedia.WikipediaPage to add the property backlinks.
"""
class Page(wikipedia.WikipediaPage):

    def __init__(self, title=None, pageid=None, redirect=True, preload=False, original_title=''):
        super(Page, self).__init__(title, pageid, redirect, preload, original_title)

    """
    This method returns the number of backlinks to a certain wikipedia article.
    """
    @property
    def backlinks(self):
        if not getattr(self, '_links', False):
            self._backlinks = [link['title'] for link in self._WikipediaPage__continued_query({'prop': 'linkshere',
                           'lhnamespace': 0, 'lhlimit': 'max'})]
        return self._backlinks


# =============================================================================
#    STATIC TYPE METHODS
# =============================================================================

def get_path(a,b):
    
    url = r"http://degreesofwikipedia.com/?a1={}&linktype=1&a2={}&skips={}&allowsideboxes=1&submit="+TOKEN+r"&currentlang=en"
    regex = r"(?<==>\s)\w+"
    with urllib.request.urlopen(url.format(a,b,b)) as html:
        encoding = html.headers['content-type'].split('charset=')[-1]
        text = str(html.read(), encoding)
        return re.findall(regex, text)


def dprint(text):
    if DEBUG:
        print("%s%s"%(DEBUG_PROMPT,text))
        