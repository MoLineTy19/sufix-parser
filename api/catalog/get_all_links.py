from utils.get_page_content import get_page_content

def get_links_from_category(url: str, limit: int = 9999, save_result: bool = False) -> dict:
    """
    Получает все ссылки из категории
    :param url: Ссылка на категорию
    :param limit: Лимит продуктов на страницу
    :param save_result: Сохранение результатов
    :return: Словарь с результатами
    """
    soup = get_page_content(url + f'?limit={limit}')
    block = soup.find('div', class_='list_showcase')

    links = []
    for link in block.find_all('a'):
        links.append(link['href'])

    if save_result:
        with open('categories_all_links.txt', 'a', encoding='utf-8') as f:
            for link in links:
                f.write(link + '\n')

    return {
        'links': links,
    }