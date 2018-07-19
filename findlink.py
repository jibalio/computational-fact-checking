
import time
start = time.clock()
cnt=0
from wikipedia_ia import Page, Path, get_path, dprint
import csv

"""
DegreesOfWikipedia.com takes in parameters with "+" instead of " ". Replace all
spaces with a PLUS sign. Make this as generic as possible.
"""

x_file = 't2_x_presidents.txt'
y_file = 't2_y_spouses.txt'
output_file = 'output/t2_spouses.csv'


o = open(output_file, 'w' , encoding="utf8", newline='')
o.write("sep=;\n")  # this will tell MS Excel that the CSV separator is ";"
csvwriter = csv.writer(o, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)

# .read() is called so that all entities in X are loaded in memory.
# so it can be reused for each loop.
ideologies = open(y_file, 'r', encoding='utf8').read()
politicians = open(x_file, 'r', encoding='utf8')
csvwriter.writerow(["Politician"]+ideologies.split(";"))

for x in politicians:
    
    rows = [x.strip()] # initial row is politician only (will append paths later)
    for y in ideologies.split(";"):
        pol = x.split()
        pol = "+".join(pol[:len(pol)])    # replace with + sign all spaces
        dprint("Getting path of %s -> %s" % (pol,y))
        a = get_path(pol, "+".join(y.split()))
        a = ">".join([x for x in a])
        print(a)
        rows.append(a)
        print(rows)
    csvwriter.writerow(rows)
o.close()

print ("Done in %.2f seconds." % (time.clock() - start))