from bs4 import BeautifulSoup


def get_cross_numbers(soup: BeautifulSoup) -> list:
    """
    Получает ОЕМ номера по продукту
    :param soup: Объект страницы (BeautifulSoup)
    :return: Словарь с ОЕМ номерами
    """
    table = soup.find('div', id='pcard-cross')

    result = []
    if table:
        inner_table = table.find('div', class_='list_showtable-wrap')
        cross_numbers = inner_table.find_all('tr')
        for cross_number in cross_numbers:
            oem = cross_number.find('td', class_='analog-brand')
            if oem:
                oem = oem.text
                result.append(oem)

    return result