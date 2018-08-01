"""
This script takes a CSV file of paths between node A to node B.
And converts them to degree values.
"""

import csv
with open('output/pathmatrices/t2_spouses.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    num_rows = 0
    degrees = dict()
    for row in csvreader:

        """
        Get the degrees of the header first
        since it would be reused everytime.
        Save in dictionary
        """
        num_rows+=1
        if num_rows = 1:
            y_axis = row[1:]
            for y in y_axis:
                if (degrees[y] != None):
                    degrees[y] = fake_GetPath(true)

        """
        Begin parse on 2nd column.
        """
        
        print (', '.join(row))
        print("------------ROW--------------")








def try_add():
    pass
def fake_GetPath(header=False):
    if header:
        return 2.52
    return 0.136
