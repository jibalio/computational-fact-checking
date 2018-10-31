
"""
Authors:
Ibalio, Jan Leryc
Alfafara, Lean
This is the backend for the C# fact checker program.
"""


import sys
from scrapers.logger import errorlog, log
import time
from PathFinder import retrieve_path, stringify_path
from Truth import get_truth_value
import argparse


"""
log("Starting grec_pathfinder.py")
parser = argparse.ArgumentParser(description='Find paths taken between articles in wikipedia using data outputted by grec_pathfinder.py. Good luck.')
parser.add_argument('sub1', help='Subject 1')
parser.add_argument('sub2', help="Subject 2")
parser.add_argument('sub3', help='Subject 3')
parser.add_argument('obj', help="Object")
args = vars(parser.parse_args())
"""

#1539052726|00d724bfd2726fd20bd241b1dc8ab49f
    
token = "1539072664|1cb61f76cefb672382503def95d2773d"


def cfc_get_truth_value(x, y, token):
    s = time.time()
    path = [x.replace('_',' ') for x in retrieve_path(x.strip(),y.strip(), token)]  #$ehdnh
    
    if len(path)==0:
        errorlog("ERROR: Could not retrieve path. Check page title spelling and make sure token has not expired.")
        path = ("undefined")
    else:
        path = stringify_path(path)
        log("Found path {}. Took {:.2f}s.".format(path, s-time.time()))
    
    
    score = get_truth_value(path, display=False)
    return score

    return cfc_get_truth_value(x, y, token)



