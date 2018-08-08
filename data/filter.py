import re

unfilteredCountries = """
Angola (Africa)
Benin (Africa)
Botswana (Africa)
Burkina Faso (Africa)
Burundi (Africa)
Cape Verde (Africa)
Central African Republic (Africa)
Comoros (Africa)
Democratic Republic of the Congo (Africa)
Republic of the Congo (Africa)
Djibouti (Africa)
Egypt (Africa)
Equatorial Guinea (Africa)
Eritrea (Africa)
Ethiopia (Africa)
Gabon (Africa)
The Gambia (Africa)
Ghana (Africa)
Guinea (Africa)
Guinea Bissau (Africa)
Kenya (Africa)
Lesotho (Africa)
Liberia (Africa)
Libya (Africa)
Madagascar (Africa)
Malawi (Africa)
Mali (Africa)
Mauritania (Africa)
Mauritius (Africa)
Morocco (Africa)
Mozambique (Africa)
Namibia (Africa)
Niger (Africa)
Nigeria (Africa)
Rwanda (Africa)
Senegal (Africa)
Seychelles (Africa)
Sierra Leone (Africa)
Somalia (Africa)
South Africa (Africa)
South Sudan (Africa)
Sudan (Africa)
Swaziland (Africa)
Tanzania (Africa)
Tunisia (Africa)
Uganda (Africa)
Zambia (Africa)
Zimbabwe (Africa)

Afghanistan (Asia)
Armenia (Asia)
Azerbaijan (Asia)
Bahrain (Asia)
Bangladesh (Asia)
Bhutan (Asia)
Brunei (Asia)
Burma (Asia)
Cambodia (Asia)
China (Asia)
Cyprus (Asia)
East Timor (Asia)
Georgia country (Asia)
India (Asia)
Indonesia (Asia)
Iran (Asia)
Iraq (Asia)
Israel (Asia)
Japan (Asia)
Jordan (Asia)
Kazakhstan (Asia)
North Korea (Asia)
South Korea (Asia)
Kuwait (Asia)
Kyrgyzstan (Asia)
Laos (Asia)
Lebanon (Asia)
Malaysia (Asia)
Mongolia (Asia)
Nepal (Asia)
Oman (Asia)
Pakistan (Asia)
State of Palestine (Asia)
Philippines (Asia)
Qatar (Asia)
Saudi Arabia (Asia)
Syria (Asia)
Tajikistan (Asia)
Thailand (Asia)
Turkey (Asia)
Turkmenistan (Asia)
United Arab Emirates (Asia)
Uzbekistan (Asia)
Vietnam (Asia)

Albania (Europe)
Andorra (Europe)
Austria (Europe)
Belarus (Europe)
Belgium (Europe)
Bosnia and Herzegovina (Europe)
Bulgaria (Europe)
Croatia (Europe)
Czech Republic (Europe)
Denmark (Europe)
Estonia (Europe)
Finland (Europe)
France (Europe)
Germany (Europe)
Greece (Europe)
Hungary (Europe)
Republic of Ireland (Europe)
Italy (Europe)
Latvia (Europe)
Liechtenstein (Europe)
Lithuania (Europe)
Republic of Macedonia (Europe)
Malta (Europe)
Monaco (Europe)
Montenegro (Europe)
Norway (Europe)
Poland (Europe)
Portugal (Europe)
Romania (Europe)
Russia (Europe)
San Marino (Europe)
Serbia (Europe)
Slovakia (Europe)
Slovenia (Europe)
Spain (Europe)
Sweden (Europe)
Switzerland (Europe)
Ukraine (Europe)
United Kingdom (Europe)

Barbados (NA)
Belize (NA)
Canada (NA)
Cuba (NA)
Dominica (NA)
Guatemala (NA)
Haiti (NA)
Honduras (NA)
Jamaica (NA)
Mexico (NA)
Kingdom of the Netherlands (NA)
Nicaragua (NA)
Panama (NA)
Saint Kitts and Nevis (NA)
Saint Lucia (NA)
Saint Vincent and the Grenadines (NA)
Trinidad and Tobago (NA)
United States (NA)

Australia (Oceania)
Fiji (Oceania)
Kiribati (Oceania)
Marshall Islands (Oceania)
Federated States of Micronesia (Oceania)
New Zealand (Oceania)
Papua New Guinea (Oceania)
Samoa (Oceania)
Solomon Islands (Oceania)
Tuvalu (Oceania)
Vanuatu (Oceania)

Argentina (SA)
Bolivia (SA)
Chile (SA)
Ecuador (SA)
Guyana (SA)
Peru (SA)
Suriname (SA)
Uruguay (SA)
Venezuela (SA)
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
Djibouti
Cairo
Malabo
Asmara
Addis Ababa
Libreville
Banjul
Accra
Conakry
Bissau
Nairobi
Maseru
Monrovia
Tripoli
Antananarivo
Lilongwe
Bamako
Nouakchott
Port Louis
Rabat
Maputo
Windhoek
Niamey
Abuja
Kigali
Dakar
Victoria Seychelles
Freetown
Mogadishu
Pretoria
Juba
Khartoum
Mbabane
Dodoma
Tunis
Kampala
Lusaka
Harare
Kabul
Yerevan
Baku
Manama
Dhaka
Thimphu
Bandar Seri Begawan
Naypyidaw
Phnom Penh
Beijing
Nicosia
Dili
Tbilisi
New Delhi
Jakarta
Tehran
Baghdad
Jerusalem
Tokyo
Amman
Astana
Pyongyang
Seoul
Kuwait City
Bishkek
Vientiane
Beirut
Kuala Lumpur
Ulan Bator
Kathmandu
Muscat Oman
Islamabad
Jerusalem
Manila
Doha
Riyadh
Damascus
Dushanbe
Bangkok
Ankara
Ashgabat
Abu Dhabi
Tashkent
Hanoi
Tirana
Andorra la Vella
Vienna
Minsk
Brussels
Sarajevo
Sofia
Zagreb
Prague
Copenhagen
Tallinn
Helsinki
Paris
Berlin
Athens
Budapest
Dublin
Rome
Riga
Vaduz
Vilnius
Skopje
Valletta
Monaco
Podgorica
Oslo
Warsaw
Lisbon
Bucharest
Moscow
City of San Marino
Belgrade
Bratislava
Ljubljana
Madrid
Stockholm
Bern
Kiev
London
Bridgetown
Belmopan
Ottawa
Havana
Roseau
Guatemala City
Port-au-Prince
Tegucigalpa
Kingston Jamaica
Mexico City
Amsterdam
Managua
Panama City
Basseterre
Castries
Kingstown
Port of Spain
Washington D.C.
Canberra
Suva
South Tarawa
Majuro
Palikir
Wellington
Port Moresby
Apia
Honiara
Funafuti
Port Vila
Buenos Aires
Sucre
Santiago
Quito
Georgetown Guyana
Lima
Paramaribo
Montevideo
Caracas
"""

#TODO make 6 randomizer for each continent
#list = africa, asia , europ, na, oceana ,sa
#   for key, value in enum(continent)

def filterContinents(countries):
    contReg = r"(\(.+)"
    continents = re.findall(contReg,countries)
    filteredContinents = {'(Africa)':[], '(Asia)':[],'(Europe)':[], '(NA)':[], '(Oceania)':[], '(SA)':[]}

    for counter, continent in enumerate(continents):
        filteredContinents[continent].append([counter,continent])

    africa = dict(filteredContinents['(Africa)'])
    asia = dict(filteredContinents['(Asia)'])
    europe = dict(filteredContinents['(Europe)'])
    na = dict(filteredContinents['(NA)'])
    oceana = dict(filteredContinents['(Oceania)'])
    sa = dict(filteredContinents['(SA)'])

    filteredAfrica = batchContinents(africa)
    filteredAsia = batchContinents(asia)
    filteredEurope = batchContinents(europe)
    filteredNa = batchContinents(na)
    filteredOceana = batchContinents(oceana)
    filteredSa = batchContinents(sa)

    newFilteredContinents = filteredAfrica, filteredAsia, filteredEurope, filteredNa, filteredOceana, filteredSa

    return newFilteredContinents

    #return filteredContinents

def filterCountries(countries):
    countReg = r".*(?=\ )"

    filteredCountries = re.findall(countReg, countries)
    filteredCountries = (list(filter(None, filteredCountries)))

    newArr = []
    for counter, country in enumerate(filteredCountries):
        newArr.append([counter, country])
    return dict(newArr)

def filterCapitals(capitals):
    filteredCapitals = capitals.splitlines()
    newArr = []
    for counter, capital in enumerate(filteredCapitals[1 :]):
        newArr.append([counter, capital])
    return dict(newArr)

def batchContinents(continent):
    filteredContinents = []

    counter = 0

    for number, capital in continent.items():
        if(counter < 6):
            filteredContinents.append([number, capital])
        counter += 1

    return dict(filteredContinents)

def matchCapCount():
    filtCount = filterCountries(unfilteredCountries)
    filtCap = filterCapitals(unfilteredCapitals)
    result = []

    for item in filtCount:
        result.append([filtCount[item], filtCap[item]])
    return result

#print(batchContinents())
print(filterContinents(unfilteredCountries))
#print(filterCapitals(unfilteredCapitals))
#print(filterCountries(unfilteredCountries))
#print(matchCapCount())
