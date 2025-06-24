from bs4 import BeautifulSoup


def get_title(soup: BeautifulSoup) -> str:
    """
    Получение названия продукта
    :param soup: Объект страницы (BeautifulSoup)
    :return: Словарь с названием
    """
    title = soup.find('div', class_='pcard-name')
    if title:
        return title.text.strip()
    else:
        return ''