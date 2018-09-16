midwest = '''
Springfield	Illinois
Indianapolis	Indiana
Des Moines	Iowa
Topeka	Kansas
Lansing	Michigan
Saint Paul	Minnesota
Jefferson City	Missouri
Lincoln	Nebraska
Bismarck	North Dakota
Columbus	Ohio
Pierre	South Dakota
Madison	Wisconsin
'''

northeast = '''
Hartford	Connecticut
Augusta Boston	Maine
Concord	Massachusetts
Albany	New York
Harrisburg	Pennsylvania
Providence	Rhode Island
Montpelier	Vermont
'''

south = '''
Montgomery	Alabama
Little Rock	Arkansas
Dover	Delaware
Tallahassee	Florida
Atlanta	Georgia U S state
Frankfort	Kentucky
Baton Rouge	Louisiana
Annapolis	Maryland
Jackson	Mississippi
Raleigh	North Carolina
Oklahoma City	Oklahoma
Columbia	South Carolina
Nashville	Tennessee
Austin	Texas
Richmond	Virginia
Charleston	West Virginia
'''

west = '''
Juneau	Alaska
Phoenix	Arizona
Sacramento	California
Honolulu Boise	Hawaii
Carson City	Nevada
Santa Fe	New Mexico
Salem	Oregon
Salt Lake City	Utah
Cheyenne	Wyoming
'''

def filterCapitals(region):
    filteredCapitals = []
    data = (list(filter(None, region.splitlines())))
    for item in data:
        temp = item.split('\t')
        filteredCapitals.append(temp[0])
    file = open("t5_x_capital.txt", "a")
    file.write('\n'.join(filteredCapitals))

def filterStates(region):
    filteredStates = []
    data = (list(filter(None, region.splitlines())))
    for item in data:
        temp = item.split('\t')
        filteredStates.append(temp[1])
    file = open("t5_x_state.txt", "a")
    file.write('\n'.join(filteredStates))


l = (midwest, northeast, south, west)
for x in l:
    filterCapitals(x)
    filterStates(x)
