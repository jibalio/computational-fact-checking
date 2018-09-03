from collections import OrderedDict
from Truth import Page
import csv

metric = []
ultrametric = []
metric_tfidf = []
ultrametric_tfidf = []

with open('data/out/i1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    colnames = []
    
    for row in reader:
        
        # These dictioanries contain the truth values in different aglorithms.
        # the keys are the ideology names in the csv file.
        # use key 'x-entity' to get hte x axis.
        row_metric = OrderedDict()
        row_ultrametric = OrderedDict()
        row_metric_tfidf = OrderedDict()
        row_ultrametric_tfidf = OrderedDict()
        
        
        colnames = row.keys()
        for key in colnames:
            row[key] = row[key].split('>')
            for idx, title in enumerate(row[key]):
                if idx!=0 and idx != len(row[key])-1:
                    Page(title, backlinksonly=True)