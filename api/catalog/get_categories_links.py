from bs4 import BeautifulSoup


def get_categories_links(soup: BeautifulSoup, save_result: bool = False) -> dict:
    """
    Получает список ссылок на категории
    :param soup: Объект страницы (BeautifulSoup)
    :param save_result: Сохранение результатов
    :return: Словарь со ссылками
    """
    block = soup.find('ul', class_='category-dropdown2-list ul0 ul-lev0')

    links = []
    if block:
        categories = block.find_all('a')
        for category in categories:
            links.append(category['href'])

    if save_result:
        with open('categories_links.txt', 'w', encoding='utf-8') as f:
            for link in links:
                f.write(link + '\n')

    return {
        'links': links,
    }