

import json
import csv

def get_entity(link):
    a = link.split("/") 
    le = a[len(a)-1]
    le = le.replace("_", " ")
    return le
cs = open('newyork.csv', 'w', encoding='utf-8', newline="")
csw = csv.writer(cs, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
csw.writerow(["Entity", "Score"])
o = open('newyork.json', 'r', encoding='utf-8')
for x in o.readlines():
    yes = 0
    j = json.loads(x)
    #print(j)
    entity = get_entity(j['evidences'][0]['url'])
    if len(j['judgments']) >5:
        continue
    for x  in j['judgments']:
        if x['judgment']=='yes':
            yes+=1
        else:
            yes-=1
    print(f"{yes}")
    csw.writerow([entity.strip(), yes])
cs.close()

