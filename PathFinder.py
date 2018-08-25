#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapers.logger import log
from scrapers.request import get_path
from scrapers.wiki_datahandler import DataHandler
import argparse
import re
import csv
import time



dh = DataHandler("wiki.sqlite3")

def get_entities(filename):
    return open(filename, 'r', encoding='utf8').read().splitlines()

def retrieve_path(x,y):
    if is_ideologies:
        x_split = x.split()
        x = " ".join(x_split[:len(x_split)-1])
    return get_path(x,y, token)

def stringify_path(lst):
    return ">".join(lst)



x_entities = []
y_entities = []
output_file = "xy.txt"
is_ideologies = False
token = ""
error_threshold = None

if __name__ == '__main__':
    # Read the parameters
    log("PathFinder.py started.")
    parser = argparse.ArgumentParser(description='Find paths taken between articles in wikipedia.')
    parser.add_argument('x', help='Path to file containing x-axis entities, separated by newlines.')
    parser.add_argument('y', help='Path to file containing y-axis entities, separated by newlines.')
    parser.add_argument('output_file', help='Where to output csv file.')
    parser.add_argument('token', help="Access token to be used when querying wikipaths.")
    parser.add_argument('-e', '--error-threshold', dest="error_threshold", default=5)
    parser.add_argument('-i', '--ideology', help="""Use if dataset to be processed is ideologies (extra-preprocessing needed). Politician outputs are expected to have target either R or D (e.g.Barack Obama (D)). The D or R target labels will be removed when searching for paths using the API, but will be retained in the outputted CSV as the axes.""", action="store_true", dest='ideology')
    args = vars(parser.parse_args())

    # get the entities
    x_entities = get_entities(args['x'])
    y_entities = get_entities(args['y'])
    if (x_entities[0].endswith('(R)') or x_entities[0].endswith('(D)')) and not args['ideology']:
        log("Warning: X-axis entities contains R/D tags.")
        print("Did you mean to put '-i' as an argument?")
        log("Terminating.")
        exit()
    output_file = args['output_file']
    is_ideologies = args['ideology']
    token = args['token']
    try:
        error_threshold = int(args['error_threshold'])
    except ValueError:
        print("Invalid value for --error-threshold.")
        exit()
   
    


    """
    CORE CODE
    """
    start = time.time()
    consecutive_error_count = 0
    
    o = open(output_file, 'w' , encoding="utf8", newline='')
    #o.write("sep=;\n")  # this will tell MS Excel that the CSV separator is ";"
    csvwriter = csv.writer(o, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    errord = False # if encountered error, set all to undefined.
    csvwriter.writerow ([""] + y_entities)   # this is the header title.
    for idx, x in enumerate(x_entities):
        if consecutive_error_count<error_threshold:
            log("Processing row {}/{}: '{}'".format(idx+1, len(x_entities), x))
        x_paths = [x.strip()]   # put x entity on x-axis in the csv
        for idx_y, y in enumerate(y_entities):
            s = time.time()
            if consecutive_error_count<error_threshold: 
                log("[R:{}/{} C:{}/{}] Getting path {} -> {}".format(idx+1, len(x_entities),idx_y+1,len(y_entities), x, y))
                path = [x.replace('_',' ') for x in retrieve_path(x.strip(),y.strip())]
            if len(path)==0:
                consecutive_error_count+=1
                # There was an error. Either page does not exist or token has expired.
                if consecutive_error_count<error_threshold:
                    log("ERROR: Could not retrieve path. Check page title spelling and make sure token has not expired.")
                else:
                    if not errord:
                        log("ERROR: Program has exceeded maximum number of consecutive errors. Something is wrong with your token. Program terminating.")
                        errord = True
                x_paths.append("undefined")
                
            else:
                x_paths.append(stringify_path(path))
                log("Found path {}. Took {:.2f}s.".format(path, s-time.time()))
                consecutive_error_count=0 #reset counter. meaning errors were isolated and not because of token error
        csvwriter.writerow(x_paths)
    log("Done in {0:.2f} seconds".format(time.time()-start))
    

    




    
























"""

import time
start = time.clock()
cnt=0
from wikipedia_ia import Page, Path, get_path, dprint
import csv


DegreesOfWikipedia.com takes in parameters with "+" instead of " ". Replace all
spaces with a PLUS sign. Make this as generic as possible.


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

"""
