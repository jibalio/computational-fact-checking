
import re
import requests
import urllib.request
import json
import wikipedia

def get_path(a,b):
    with urllib.request.urlopen(url.format(a,b)) as html:
        encoding = html.headers['content-type'].split('charset=')[-1]
        text = str(html.read(), encoding)
        return re.findall(regex, text)