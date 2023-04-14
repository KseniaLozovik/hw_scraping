import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import re

def get_headers():
    return Headers(browser="firefox", os="win").generate()


def get_text(url):
    return requests.get(url, headers=get_headers()).text


HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

response = get_text(HOST)
soup = BeautifulSoup(response, features='lxml')
lenta = soup.find(id='a11y-main-content')
vacancy = lenta.findAll(class_='vacancy-serp-item__layout')
vacancy_list = []

for i in vacancy:
    # print(i)
    result = {}
    title = i.find(class_='serp-item__title')
    link_tag = title['href']
    result.update({'Url': link_tag})
    response = get_text(link_tag)
    soup = BeautifulSoup(response, features='lxml')
    name = soup.find(class_='bloko-header-section-1').text
    result.update({'title': name})
    description = soup.find(class_='vacancy-description').text
    print(description)
    if 'django' in description and 'flask' in description:
        print('match')



