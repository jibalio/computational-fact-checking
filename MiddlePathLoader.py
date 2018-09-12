from collections import OrderedDict
from Truth import Page
import csv

metric = []
ultrametric = []
metric_tfidf = []
ultrametric_tfidf = []

with open('data/out/t3_countries.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    colnames = []
    
    for idx, row in enumerate(reader):
        if idx==0:
            continue
        # These dictioanries contain the truth values in different aglorithms.
        # the keys are the ideology names in the csv file.
        # use key 'x-entity' to get hte x axis.
        row_metric = OrderedDict()
        row_ultrametric = OrderedDict()
        row_metric_tfidf = OrderedDict()
        
        row_ultrametric_tfidf = OrderedDict()
        
        
        
        colnames = row.keys()
        for key in list(colnames)[1:]:
            row[key] = row[key].split('>')
            for idx, title in enumerate(row[key]):
                if idx!=0 and idx != len(row[key])-1:
                    Page(title, backlinksonly=True)
                else:
                    Page(title, backlinksonly=False)