
"""
grec_extractor.py
written by Alfafara, Lean; Ibalio, Jan
This script extracts GREC statements from a grec file in json format,
and outputs 3 files in 1 folder:
    grec_folder/
        - x.txt (for Pathfinding purposes)
        - y.txt (for Pathfinding purposes)
        - ground_truth.csv (contains columns Statement, Graph)
"""

import json
import csv
import urllib.parse
import re
from scrapers.utils import mkdir
from scrapers.request import get_htmlresponse
from scrapers.wiki_datahandler import DataHandler
import argparse



dh = DataHandler('wiki.sqlite3')

def get_entity(link):
    a = link.split("/") 
    le = a[len(a)-1] # get only the last element http:/www.wikipediea.org/ARTICLE_TITLE
    le = le.replace("_", " ") 
    return urllib.parse.unquote(le) # to remove url quoted strings

def get_grec_score(judgments):
    yes = 0
    for x in judgments:
        if x['judgment']=='yes':
            yes+=1
        else:
            yes-=1
    return yes

def getwikititle (mid):
    quoted_mid = urllib.parse.quote(mid)
    requrl = f"https://www.wikidata.org/w/index.php?title=Special:Search&profile=default&search=haswbstatement%3AP646%3D{quoted_mid}&fulltext=0&searchToken=e038oxtyk6jb3s623aqu20u90"
    #print(requrl)
    response = get_htmlresponse(requrl)
    r=None
    try:
        r = re.findall(r'(?<=<span class="wb-itemlink-label" lang="en" dir="ltr">).+(?=<\/span> <span class="wb-itemlink-id">)', response)[0]
    except:
        r = None
    return r

import time
from scrapers.logger import log, errorlog


if __name__ == "__main__":

    log("The GREC genie has been freed from the bottle. Starting grec_extractor.py")
    parser = argparse.ArgumentParser(description='Find paths taken between articles in wikipedia.')
    parser.add_argument('grec_path', help='path to GREC json file to extract data from.')
    parser.add_argument('output_folder', help='NAME OF THE OUTPUT FOLDER. Not a path. All outputs will be stored in data/GREC by default.')
    args = vars(parser.parse_args())

    # Get the command line arguments.
    source = args['grec_path']
    out = args['output_folder']

    # Create the necessary directories.
    mkdir('data')
    output_path = f'data/GREC/{out}'
    mkdir(output_path)

    x_file = f"{output_path}/paths.txt"

    xo = open(x_file, 'a', encoding='utf-8')
    #yo = open(y_file, 'a', encoding='utf-8')
    xo.write("")
    xo.close()
    #yo.write("")

    cs = open(f'{output_path}/ground_truth.csv', 'w', encoding='utf-8', newline="")
    o = open(source, 'r', encoding='utf-8')
    csw = csv.writer(cs, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csw.writerow(["subject", "predicate", "object", "score"])

    stream = o.readlines()
    for idx, x in enumerate(stream):
        s = time.time()
        
        # read each line in the GREC json.
        j = json.loads(x)

        # if there are more than 5 ratings, discard the data
        # (erroneous data) INCLUDE IN METHODOLOGY.
        if len(j['judgments']) >5:
            continue
        
        subject = get_entity(j['evidences'][0]['url'])
        predicate = j["pred"]
        object_mid = j['obj']   # this is the freebase MID of the object entity
        obj_title = None
        is_dirty_data = False
        
        log(f"[{idx+1}/{len(stream)}] Retrieving (`{subject}`, `{predicate}`, `{object_mid}`)")

        is_notfound = False
        try:
            obj_title = dh.get_mid_title(object_mid) # try if naa sa database ang title sa MID
            if obj_title == "_invalid_mid":
                is_dirty_data = True
            if not is_dirty_data:
                log(f"grec_extractor.py: MID {object_mid} is in database")
            else: 
                errorlog(f"Data in DB, but was {object_mid} as invalid. Discarding data.")
            log(f"Operation done in {time.time()-s} s.")
        except:
            log(f"grec_extractor.py: MID {object_mid} NOT found. Querying Wikidata.")
            is_notfound = True
            
        if is_notfound:
            try:
                obj_title = getwikititle(object_mid)
                dh.add_mid(object_mid, obj_title)
                log(f"Done. Remembered MID! Operation done in {time.time()-s} s.")
            except:
                errorlog(f"ERROR: There is no such MID {object_mid} in the database. Discarding data")
                dh.add_mid(object_mid, "_invalid_mid")
                is_dirty_data = True

        if is_dirty_data:
            continue
            
        # get the name of the subject entity.

        
        
        # get the GREC score [-5, +5]
        yes = get_grec_score(j['judgments'])
        print(f"{yes}")
        csw.writerow([subject.strip(), predicate, obj_title, yes])
        
        #xo = open(x_file, 'a', encoding='utf-8')
        #yo = open(y_file, 'a', encoding='utf-8')
        #xo.write(f"{subject}\n")
        #xo.close()
        #yo.write(f"{obj_title}\n")
        
    cs.close()







