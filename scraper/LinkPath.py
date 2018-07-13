import re
import request
import urllib.request
import json

from lib.wikipedia import Wikipedia
from lib.wiki2plain import Wiki2Plain


"""
Returns a list of page titles that were traversed when searching.
"""
url = r"http://degreesofwikipedia.com/?a1={}&linktype=1&a2={}&skips=&allowsideboxes=1&submit=1531322990|0807da41fa5f9d76798d50fc9b9378bc&currentlang=en"
regex = r"(?<==>\s)\w+"
def get_path(a,b):
    with urllib.request.urlopen(url.format(a,b)) as html:
        encoding = html.headers['content-type'].split('charset=')[-1]
        text = str(html.read(), encoding)
        return re.findall(regex, text)

"""
Gets the numberical frequency of in-degrees to that node using WIkipedia API
"""
wikifreq_api = r"https://en.wikipedia.org/w/api.php?action=query&list=backlinks&bltitle={}&bllimit=600&blfilterredir=nonredirects&format=json"
def get_backlink_count(page_title):
    r = requests.get(wikifreq_api.format(page_title))
    return len(r.json()["query"]["backlinks"])

def get_path_degrees(a,b):
    backlinks = []
    path = get_path(a,b)
    for x in path:
        x.replace("_"," ")
        backlinks.append(get_backlink_count(x))
    return list(zip(path, backlinks))

def get_link_count():
    r = requests.get(r"https://en.wikipedia.org/w/api.php?action=query&titles=Athens&prop=links&format=json&pllimit=500")
    return len(r.json()["query"]["pages"]["1216"]["links"])

def get_instance(article, word):
    return article.lower().count(word)

def get_article(name):
    lang = 'simple'
    wiki = Wikipedia(lang)

    try:
        raw = wiki.article(name)
    except:
        raw = None

    if raw:
        wiki2plain = Wiki2Plain(raw)
        content = wiki2plain.text
    return content

# Test get path
#print(get_backlink_count("French fries"))
#print(get_path("Jose_Rizal", "Liberalism"))
print(get_link_count())

# Test get links
#print (get_backlink_count("French Fries"))
