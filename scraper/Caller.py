import urllib2
url = r"http://degreesofwikipedia.com/?a1=Jos%C3%A9+Rizal&linktype=1&a2=Islam&skips=&allowsideboxes=1&submit=1531118388%7Cb241f1d8881cf4550f70bb60deea470b&currentlang=en"
f = urllib.urlopen(url)
print (f.read())
