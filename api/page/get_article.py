from bs4 import BeautifulSoup


def get_article(soup: BeautifulSoup) -> str:
    """
    Получение артикула товара
    :param soup: Объект страницы (BeautifulSoup)
    :return: Словарь с артикулом
    """
    article = soup.find('div', class_='pcard-model')

    if article:
        clear_article = article.text.strip().split(' ')[1]
        return clear_article
    else:
        return ''