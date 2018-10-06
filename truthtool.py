from wikipedia import WikipediaPage, page
from scrapers.request import get_response, get_path
from scrapers.wiki_datahandler import DataHandler
from scrapers.logger import log, errorlog
import time
import math
import urllib
import wikipedia
from PathFinder import retrieve_path
from nlp import LemTokens, LemNormalize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np
from Truth import Page

def gtv(path_taken, display=False):
    #print(path_taken)
    # slice the path
    s = time.time()
    if display:
        log(f"path_taken: '{path_taken}'")
    path = [Page(d, display=display) for d in path_taken.split('>')]
    source = path[0] # get the first element of the path
    dest = path[len(path)-1] # get the last element of the path
    #----------------------------------------------------------------------
    documents = [source.pagecontent, dest.pagecontent]
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    def cos_similarity(textlist):
        tfidf = TfidfVec.fit_transform(textlist)
        return (tfidf * tfidf.T).toarray()
    
    cos_sim = cos_similarity(documents)
    # ---------------------------------------------------------------------
    cos_sim = cos_sim[0][1]
    truthvalue = 1.00
    for x in path[1:]:
        print(f"{x.backlinkcount}*{cos_sim}")
        truthvalue+=math.log(x.backlinkcount*(cos_sim))
    # ---------------------------------------------------------------------
    truthvalue = 1/truthvalue
    truthvalue*=0.5
    truthvalue+=cos_sim*0.5
    return truthvalue

path = "Arthur Wakefield>Essex>England>London"
print(gtv(path))

