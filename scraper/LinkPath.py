import re

def get_path(phparray):
    return re.findall('(?<==>\s)\w+', phparray)
