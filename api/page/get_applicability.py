from bs4 import BeautifulSoup


def get_applicability(soup: BeautifulSoup) -> list:
    """
    Получает применимости по продукту
    :param soup: Объект страницы (BeautifulSoup)
    :return: Словарь с применимостями
    """
    block = soup.find('div', class_='applicabilit-group-list')

    result = []
    if block:
        applicability_list = block.find_all('a')

        if applicability_list:
            for applicability in applicability_list:
                appl = ''.join(applicability.text.strip().split('\n'))
                result.append(appl)

    return result