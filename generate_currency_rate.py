from datetime import date, timedelta
from lxml import html, etree
import requests
import os.path


START_DATE = date(2018, 1, 1)
END_DATE = date(2018, 3, 1)
CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="
CURRENCY = ["USD", "TRY", "CNY", "CAD", "JPY", "EUR", "NOK", "GBP"]
         

def getDateList(start, end):
    delta = end - start
    date_list = []
    for i in range(delta.days + 1):
        date_list.append(start + timedelta(i))
    return date_list


def loadXmlListFromCbr(date_list):
    xml_list = []
    if date_list:
        for i in date_list:
            try:
                response = requests.get(f'{CBR_URL}{i.strftime("%d/%m/%Y")}')
                xml_list.append(response.text)
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
        return xml_list
    return xml_list


def getXmlList(date_list):
    if os.path.exists("xml_list.txt"): 
        with open("xml_list.txt", 'r') as f:
            xml_list = [line.rstrip('\n') for line in f]
    else:
        xml_list = loadXmlListFromCbr(date_list)
        with open("xml_list.txt", 'w') as f:
            for s in xml_list:
                f.write(str(s) + '\n')
    return xml_list


def createStr(xml_list, date_list):
    temp = "id_currency, [date], rate\n"

    for i, row in enumerate(xml_list):
        root = html.fromstring(bytes(row, encoding='utf-8'))

        flag = False
        for val_curs in root.getchildren():
            for elem in val_curs.getchildren():
                if (elem.tag.lower() == "charcode") and (not flag):
                    if elem.text in CURRENCY:
                        flag = True
                        temp = f"{temp}{elem.text}, "
                else:
                    if (elem.tag.lower() == "value") and (flag):
                        temp = f"{temp}{date_list[i].strftime('%d-%m-%Y')}, {elem.text.replace(',', '.')}\n"
                        flag = False

    return temp[:-1]


def save_sql():
    values = createStr(xml_list, date_list)
    with open('currency_rate.csv', 'w') as file:
        file.write(values)


date_list = getDateList(START_DATE, END_DATE)
xml_list = getXmlList(date_list)
save_sql()
