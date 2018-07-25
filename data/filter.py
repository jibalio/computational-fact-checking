import re

regex = r".*(?=\ )"

unfilteredCountries = """
Angola (Africa)
Benin (Africa)
Botswana (Africa)
Burkina Faso (Africa)
Burundi (Africa)
"""

unfilteredCapitals = """
Luanda
Porto-Novo
Gaborone
Ouagadougou
Bujumbura
Praia
Bangui
Moroni Comoros
Kinshasa
Brazzaville
"""

def filterCountries(countries):
    filteredCountries = re.findall(regex, countries)
    filteredCountries = (list(filter(None, filteredCountries)))
    newArr = []
    for counter, country in enumerate(filteredCountries):
        newArr.append([counter, country])
    return dict(newArr)

def filterCapitals(capitals):
    filteredCapitals = capitals.split('\n')
    newArr = []
    for counter, capital in enumerate(filteredCapitals[1 : -1]):
        newArr.append([counter, capital])
    return dict(newArr)

def matchCapCount():
    filtCount = filterCountries(unfilteredCountries)
    filtCap = filterCapitals(unfilteredCapitals)
    result = []
    for item in filtCount:
        result.append([filtCount[item], filtCap[item]])
    return result

print(matchCapCount())
