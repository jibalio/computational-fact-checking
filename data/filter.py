import re

regex = r"\w+(?=\s* [^/])"

countries = """
Angola (Africa)
Benin (Africa)
Botswana (Africa)
Burkina Faso (Africa)
Burundi (Africa)
"""

def filterCountries(countries):
    filteredCountries = re.findall(regex, countries)
    return dict([counter + 1,country for counter, country in enumerate(filteredCountries)])

print(filterCountries(countries))
