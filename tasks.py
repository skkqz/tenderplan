import requests
import xmltodict
from bs4 import BeautifulSoup
from config import cookies, headers
from celery_settings import app

@app.task
def get_links_to_printable_form() -> list[str]:
    """Получить ссылки на печатную форму закупки"""

    links_list = []

    for page_num in range(1, 3):

        url = f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber={page_num}'
        response = requests.get(url=url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        soup_links_all = soup.find_all('div', class_='w-space-nowrap ml-auto registry-entry__header-top__icon')

        for link in soup_links_all:
            link_test = link.find('a', {'target': "_blank"})['href']
            replace_link = link_test.replace('view.html', 'viewXml.html')
            links_list.append(f'https://zakupki.gov.ru/{replace_link}')

    return links_list


@app.task
def get_data_from_xml(link_list: list[str]):
    """Парсинг данных из xml"""

    for link_xml in link_list:

        response = requests.get(url=link_xml, cookies=cookies, headers=headers)

        dict_data = xmltodict.parse(response.text)
        list_key_dict = list(dict_data.keys())
        print(dict_data[list_key_dict[0]]['commonInfo'].get('publishDTInEIS', None))
