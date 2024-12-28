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

data_list = []

for item in data:
    country_name = item["name"]["official"]
    country_code = item["cca3"] 
    country_independence_status = item.get("independent","Status not found")
    country_currency = get_currency(item)
    country_capital = get_capital(item)
    country_region = item["region"]
    country_subregion = get_subregion(item)
    country_languages = get_languages(item)
    country_latitude = get_latitude(item)
    country_longitude = get_longitude(item)
    country_landlock_status = item["landlocked"]
    country_borders = get_borders(item)
    country_area = item["area"]
    country_location = item["maps"]["googleMaps"] 
    country_population = item["population"]
    country_car_sign = get_car_signs(item)
    country_car_side = item["car"]["side"]
    country_timezones = ', '.join(item["timezones"])
    country_continents = ' '.join(item["continents"])
    country_flag = item["flags"][1]
    country_ltd = get_tld(item)

    data_list.append([country_name,country_code,country_independence_status,country_currency,
                      country_capital,country_region,country_subregion,country_languages,
                      country_latitude,country_longitude,country_landlock_status,country_borders,
                      country_area,country_location,country_population,country_car_sign,country_car_side,
                      country_timezones,country_continents,country_flag,country_ltd])
    
    
df = pd.DataFrame(data_list,columns=[country_name,country_code,country_independence_status,country_currency,
                      country_capital,country_region,country_subregion,country_languages,
                      country_latitude,country_longitude,country_landlock_status,country_borders,
                      country_area,country_location,country_population,country_car_sign,country_car_side,
                      country_timezones,country_continents,country_flag,country_ltd])

df.to_csv('teste.csvs')
    






