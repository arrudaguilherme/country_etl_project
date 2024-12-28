import requests, json
import pandas as pd

continents = ['america','europe','asia','africa','oceania']
# https://restcountries.com/v3.1/all
# https://restcountries.com/v3.1/region/america

URL = 'https://restcountries.com/v3/all'

request = requests.get(URL)

response = request.json()

data = response

def get_currency(item:dict):
    currencies = item.get("currencies")
    if not currencies:
        return "Currency not found"
    for i in currencies:
        return i

def get_capital(item:dict):
    capitals = item.get("capital")
    if not capitals:
        return "Capital not found"
    for i in capitals:
        return i

def get_subregion(item:dict):
    subregions = item.get("subregion")
    if not subregions:
        return "Subregion not found"
    return subregions

def get_languages(item:dict):
    lang_list = []
    languages = item.get("languages")
    if not languages:
        return "Languages not found"
    for i in languages:
        lang_list.append(i)
    result = ', '.join(lang_list)
    return result

def get_latitude(item:dict):
    lat_long = item.get("latlng")
    if not lat_long:
        return "Latlng not found"
    return lat_long[0]

def get_longitude(item:dict):
    lat_long = item.get("latlng")
    if not lat_long:
        return "Latlng not found"
    return lat_long[1]

def get_borders(item:dict):
    borders = item.get("borders")
    if not borders:
        return "Borders not found"
    result = ', '.join(borders)
    return result

def get_car_signs(item:dict):
    car = item.get("car")
    if not car:
        return "Information not found"
    for i in car.values():
        if i == ' ' or i == None:
            return "Information not found"
        result = ', '.join(i)
        return result

def get_tld(item:dict):
    tlds = item.get("tld")
    if not tlds:
        return "Information not found"
    return tlds[0]

for item in data:
    print(item["name"]["official"]) #name
    print(item["cca3"]) #code
    print(item.get("independent","Status not found")) # independent
    print(get_currency(item))
    print(get_capital(item))
    print(item["region"])
    print(get_subregion(item))
    print(get_languages(item))
    print(get_latitude(item))
    print(get_longitude(item))
    print(item["landlocked"])
    print(get_borders(item))
    print(item["area"])
    print(item["maps"]["googleMaps"]) #google maps
    print(item["population"])
    print(get_car_signs(item))
    print(item["car"]["side"])
    print(', '.join(item["timezones"]))
    print(' '.join(item["continents"]))
    print(item["flags"][1])
    print(get_tld(item))
    print("########################")





