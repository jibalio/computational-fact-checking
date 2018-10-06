

import json
import csv


entities = dict()

cs = open('highests.csv', 'w', encoding='utf-8', newline="")
csw = csv.writer(cs, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

csw.writerow(["Entity", "Score"])

o = open('20131104-education-degree.json', 'r', encoding='utf-8')
for x in o.readlines():
    print(x)
    j = json.loads(x)

    if j['obj'] not in entities:
    	entities[j['obj']] = 0
    else:
    	entities[j['obj']]+=1


for x in entities:
    csw.writerow([x, entities[x]])



cs.close()

