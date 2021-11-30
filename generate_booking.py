from datetime import date, timedelta
import random


START_DATE = date(2018, 1, 1)
END_DATE = date(2018, 3, 1)
COUNTRIES = (
    {"tag": "russia", "k": 1, "currency": "RUB",}, {"tag": "usa", "k": 57, "currency": "USD",},
    {"tag": "turkey", "k": 15, "currency": "TRY",}, {"tag": "china", "k": 88, "currency": "CNY",},
    {"tag": "mexico", "k": 3, "currency": "MXN",}, {"tag": "canada", "k": 45, "currency": "CAD",},
    {"tag": "japan", "k": 50, "currency": "JPY",}, {"tag": "austria", "k": 69, "currency": "EUR",},
    {"tag": "great_britain", "k": 78, "currency": "GBP",}, {"tag": "germany", "k": 69, "currency": "EUR",},
    {"tag": "malaysia", "k": 14, "currency": "MYR",}, {"tag": "thailand", "k": 1.7, "currency": "THB",},
    {"tag": "italy", "k": 69, "currency": "EUR",}, {"tag": "greece", "k": 69, "currency": "EUR",},
    {"tag": "france", "k": 69, "currency": "EUR",}, {"tag": "spain", "k": 69, "currency": "EUR",},
    {"tag": "finland", "k": 69, "currency": "EUR",}, {"tag": "portugal", "k": 69, "currency": "EUR",},
    {"tag": "netherlands", "k": 69, "currency": "EUR",}, {"tag": "norway", "k": 70, "currency": "NOK",}
)
SOURCES = (
    "BS-CHANNEL_MANAGER", "TL-CHANNEL_MANAGER", "BL-CHANNEL_MANAGER", "RC-CHANNEL_MANAGER", "CH-CHANNEL_MANAGER",
    "GB-CHANNEL_MANAGER", "BNOVO-CHANNEL_MANAGER", "OMS-CHANNEL_MANAGER", "KK-CHANNEL_MANAGER", "AS-CHANNEL_MANAGER"
)


def getDateList(start, end):
    delta = end - start
    date_list = []
    for i in range(delta.days + 1):
        date_list.append(start + timedelta(i))
    return date_list


def generate_values(country, autoincrement):
    result = ""
    date = random.choice(list_dates)
    start_date = date + timedelta(random.randint(3, 20))
    nights = random.randint(1, 30)
    price = nights * (random.randint(2000, 20000) / country["k"])
    currency = country["currency"]
    source = SOURCES.index(random.choice(SOURCES)) + 1
    if SOURCES[source - 1] != "BS-CHANNEL_MANAGER":
        creator = ""
    else:
        creator = random.choice(["BGC", "ETC"])
    result = f"{autoincrement},{random.randint(1, 10000)},{date.strftime('%d-%m-%Y')},{start_date.strftime('%d-%m-%Y')}," \
             f"{random.randint(1, 6)},{nights},{round(price, 4)},{currency},{source},{creator}\n"
    return result


list_dates = getDateList(START_DATE, END_DATE)


# P.S. Лучше было через BULK INSERT
def create_queries():        
    start_query = "id_booking,id_provider,creation_date,start_date,status,nights,price, " \
                  "id_currency,id_source,creator\n"
    result = ""
    autoincrement = 1
    for i, country in enumerate(COUNTRIES):
        print(f"{i+1}. {country['tag']} - generating...")
        x = 0
        count = 25000
        while x < count:
            if x == 0 and i == 0:
                result = f"{start_query}{generate_values(country, autoincrement)}"
            else:
                result = f"{result}{generate_values(country, autoincrement)}"
            x += 1
            autoincrement += 1
    return result[:-1]


result = create_queries()
with open("booking.csv", "w") as file:
    file.write(result)
