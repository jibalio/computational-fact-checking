"""
Extra utilities
"""

import urllib
import urllib.request
from urllib.parse import quote_plus
import re

def get_response(url):
    with urllib.request.urlopen(url) as html:
        encoding = html.headers['content-type'].split('charset=')[-1]
        text = str(html.read(), encoding)
    return float(text)


def get_path(a,b, token):
    url = r"http://degreesofwikipedia.com/?a1={}&linktype=1&a2={}&skips={}&allowsideboxes=1&submit="+token+r"&currentlang=en"
    regex = r".+ was not a valid article|(?<==>\s).+"
    with urllib.request.urlopen(url.format(quote_plus(a),quote_plus(b),quote_plus(b))) as html:
        encoding = html.headers['content-type'].split('charset=')[-1]
        text = str(html.read(), encoding)
        return re.findall(regex, text) 


