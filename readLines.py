Truth import Page
def readLines(file):
    content = open(file).readlines()
    for line in content:
        page(line)
