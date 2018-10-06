from Truth import Page
import pandas as pd
filename = "data/GREC/GREC_degree/gt_with_paths.csv"
a = pd.read_csv(filename, sep=';')
c = a['path']
d = list(c)
for idx, x in enumerate(d):
    print(f'[{idx+1}/{len(d)}]')
    elist = x.split(">")
    for a, entity in enumerate(elist):
        cx = entity[0].upper() + entity[1:]
        try:
            if a==0 or a==len(elist)-1:
                Page(cx,backlinksonly=False)
            else:
                Page(cx,backlinksonly=True)

        except:
            pass