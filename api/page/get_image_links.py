from bs4 import BeautifulSoup


def get_image_links(soup: BeautifulSoup, size: int = 800) -> list:
    """
    Получает ссылки на изображения продукта
    :param soup: Объект страницы (BeautifulSoup)
    :param size: Размер изображения. По умолчанию 800.
    :return: Словарь со ссылками
    """
    image_block = soup.find('div', id='pcard-images-thumbs-list')

    links = []
    if image_block:
        image_links = image_block.find_all('img')

        if image_links:
            for image_link in image_links:
                links.append(image_link['src'].replace('127x127', f'{size}x{size}'))
    return links