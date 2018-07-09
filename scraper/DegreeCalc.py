import requests
import json

api_call = r"https://en.wikipedia.org/w/api.php?action=query&list=backlinks&bltitle=Main%20Page&bllimit=5&blfilterredir=redirects&format=json"
print ('requesting %s' % api_call)

solditems = requests.get('api_call') # (your url)
data = solditems.json()
with open('data.json', 'w') as f:
    json.dump(data, f)