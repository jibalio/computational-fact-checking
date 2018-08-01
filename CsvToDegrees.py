"""
This script takes a CSV file of paths between node A to node B.
And converts them to degree values.
"""
def fake_GetPath(header=False):
    if header:
        return 2.52
    return 0.136


import csv
with open('output/pathmatrices/t2_spouses.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    current_row_idx = 0
    degrees = dict()
    
    for d in csvreader:
        

        # Ignore separator column
        if 'sep=' in d:
            continue
        
        row = d[1:]
        
        
        
        
        entities = [x.split('>') for x in row]

        """
        # run this if header row.
        current_row_idx += 1
        if current_row_idx == 1:
            for x in entities:
                if x[
                print(x[0])
        """

        # SKIP FIRST ROW
        current_row_idx += 1
        if current_row_idx == 1:
            continue

        degree_row_x = []
        for path in entities:
            
            for entity in path:

                ## if entity is not recorded in dictionary
                ## try to calculate before accessing
                if entity not in degrees:
                    degrees[entity] = fake_GetPath()

                ## in this part, degree of entity is guaranteed
                ## to exist

            pathdeg = ([str(degrees[a]) for a in path])
            pathdeg = ">".join(pathdeg)
            degree_row_x.append(pathdeg)

        print(degree_row_x)
        print("%s\n----------------------------" % entities)









def try_add(key):
    if key not in degrees:
        degrees[key] = fake_GetPath()
        

