from bs4 import BeautifulSoup


def get_categories(soup: BeautifulSoup) -> list:
    """
    Получение категории и подкатегории продукта
    :param soup: Объект страницы (BeautifulSoup)
    :return: Словарь с категориями
    """
    categories_block = soup.find('div', id='breadcrumbs')

    category_list = []
    if categories_block:
        categories = categories_block.find_all('span', itemprop='name')

        if categories:
            for category in categories:
                if category.text != 'Главная':
                    category_list.append(category.text)

    if len(category_list) > 1:
        return [category_list[0], category_list[1]]
    elif len(category_list) == 1:
        return [category_list[0], '']
    else:
        return ['', '']