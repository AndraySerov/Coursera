from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    params = {'date_req': date}
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'xml')
    val_to, nom_to = get_course(cur_to, soup)  # get nominal and value

    if cur_from == 'RUR':
        return (amount / val_to * nom_to).quantize(Decimal('.0001'))

    val_from, nom_from = get_course(cur_from, soup)
    return (amount * val_from * nom_to /
            (val_to * nom_from)).quantize(Decimal('.0001'))


def get_course(valute, soup):
    val = soup.find('CharCode', text=valute).find_next_sibling('Value').string
    nom = soup.find('CharCode', text=valute).find_next_sibling('Nominal').string
    return (Decimal(val.replace(',', '.')), Decimal(nom.replace(',', '.')))
