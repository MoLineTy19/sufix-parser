import requests
from bs4 import BeautifulSoup


def get_page_content(url: str) -> BeautifulSoup:
    """
    Получает объект страницы в BeautifulSoup
    :param url: Ссылка на страницу
    :return: Объект страницы
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup