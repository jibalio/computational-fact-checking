import urllib.request
import re

url = r"http://degreesofwikipedia.com/?a1={}&linktype=1&a2={}&skips=&allowsideboxes=1&submit=1531118388%7Cb241f1d8881cf4550f70bb60deea470b&currentlang=en"
regex = r"Array\n\([\s\S]+\n\)"
def GetPath(a,b):
    with urllib.request.urlopen(url.format(a,b)) as html:
        encoding=html.headers['content-type'].split('charset=')[-1]
        text = str(html.read(), encoding)
        return (re.findall(regex, text)[0])

print (GetPath("Ted+Cruz", "Islam"))
