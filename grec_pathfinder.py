"""GREC PATHFINDER
This will take in a csv, 
and output a list of paths.
"""
import pandas as pd
from scrapers.logger import log
import csv
from PathFinder import retrieve_path, stringify_path
import time
import argparse



if __name__ == "__main__":

    log("Starting grec_pathfinder.py")
    parser = argparse.ArgumentParser(description='Find paths taken between articles in wikipedia using data outputted by grec_pathfinder.py. Good luck.')
    parser.add_argument('output_tag', help='tag you used in grec_extractor.py')
    parser.add_argument('token', help="Access token to be used when querying wikipaths.")
    args = vars(parser.parse_args())

    token = args['token']
    filename = "gt_with_paths.csv"
    outputfile = f"data/GREC/{args['output_tag']}/{filename}"

    
    csvfile = open(outputfile, 'w', encoding='utf-8', newline="")
    gt = f"data/GREC/{args['output_tag']}/ground_truth.csv"
    a = pd.read_csv(gt, sep=';')

    csw = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csw.writerow(["subject", "predicate", "object", "score", 'path'])

    cx = lambda x, y: [x]
    consecutive_error_count = 0
    for index, row in a.iterrows():
        s = time.time()
        x = row['subject']
        y = row['object']
        
        log(f"[{index+1}/{len(a)}] {x} -> {y}.")
        path = [x.replace('_',' ') for x in retrieve_path(x.strip(),y.strip(), token)]  #$ehdnh
        
        if len(path)==0:
            log("ERROR: Could not retrieve path. Check page title spelling and make sure token has not expired.")
            path = ("undefined")
        else:
            path = stringify_path(path)
            log("Found path {}. Took {:.2f}s.".format(path, s-time.time()))
        csw.writerow([x, row['predicate'], y, row['score'], path])
        
        


    


