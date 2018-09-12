Truth import Page

def readLines(file):
    content = open(file).readlines()
    for line in content:
        try:
            Page(line)
        except:
            pass
