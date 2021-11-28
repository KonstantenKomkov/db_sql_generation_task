from bs4 import BeautifulSoup
import requests
import random


COUNTRIES = (
    {"tag": "russia", "id": 1,}, {"tag": "usa", "id": 2,},
    {"tag": "turkey", "id": 3,}, {"tag": "china", "id": 4,},
    {"tag": "mexico", "id": 5,}, {"tag": "canada", "id": 6,},
    {"tag": "japan", "id": 7,}, {"tag": "austria", "id": 8,},
    {"tag": "great_britain", "id": 9,}, {"tag": "germany", "id": 10,},
    {"tag": "malaysia", "id": 11,}, {"tag": "thailand", "id": 12,},
    {"tag": "italy", "id": 13,}, {"tag": "greece", "id": 14,},
    {"tag": "france", "id": 15,}, {"tag": "spain", "id": 16,},
    {"tag": "finland", "id": 17,}, {"tag": "portugal", "id": 18,},
    {"tag": "netherlands", "id": 19,}, {"tag": "norway", "id": 20,})


def getLink(i, country):
    URL = 'https://www.tursvodka.ru/countries/'
    TAG = 'hotels'
    if i == 0:
        return f"{URL}{country}/{TAG}/"
    else:
        return f"{URL}{country}/{TAG}/p/{i+1}/"
    

def load_hotels(country):
    names = []
    count = 500
    i = 0
    while len(names) < count:
        try:
            response = requests.get(getLink(i, country))
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.findAll("div", {"class": "hotel__descript-name"})
        for a in divs:
            if a.a.text not in names: 
                names.append(a.a.text)
            
        i += 1
    return names[:count]


def create_SQL_values(hotels_by_countries):
    
    sql_text = "INSERT INTO dbo.provider (country_id, city_id, provider_name) VALUES "
    result = ""
    for i, hotels in enumerate(hotels_by_countries):
        if i == 0:
            result = f"{sql_text}"
            for hotel in hotels:
                name = hotel.replace("'", '"')
                result = f"{result}({i+1}, {random.randint(i*15+1, i*15+15)}, '{name}'), "
        else:
            if i % 2 == 0:
                result = f"{result[:-2]}\n{sql_text}"
                for hotel in hotels:
                    name = hotel.replace("'", '"')
                    result = f"{result}({i+1}, {random.randint(i*15+1, i*15+15)}, '{name}'), "
            else:
                for hotel in hotels:
                    name = hotel.replace("'", '"')
                    result = f"{result}({i+1}, {random.randint(i*15+1, i*15+15)}, '{name}'), "
    return result[:-2]

    
    
hotels_by_countries = []
for i, country in enumerate(COUNTRIES):
    print(f"{i+1}. {COUNTRIES[i]['tag']} + ")
    hotels_by_countries.append(load_hotels(country["tag"]))

result = create_SQL_values(hotels_by_countries)
with open("provider INSERT.txt", "w") as file:
    file.write(result)

