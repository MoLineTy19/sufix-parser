from api.page.get_applicability import get_applicability
from api.page.get_article import get_article
from api.page.get_categories import get_categories
from api.page.get_cross_numbers import get_cross_numbers
from api.page.get_image_links import get_image_links
from api.page.get_title import get_title
from utils.get_page_content import get_page_content


def get_page(url: str) -> dict:
    """
    Получает данные о странице по ссылке
    :param url: Ссылка на страницу
    :return: Словарь с данными о странице
    """
    soup = get_page_content(url=url)
    category, sub_category = get_categories(soup=soup)
    title = get_title(soup=soup)
    article = get_article(soup=soup)
    applicability = get_applicability(soup=soup)
    cross_numbers = get_cross_numbers(soup=soup)
    image_links = get_image_links(soup=soup)

    return {
        'url': url.strip(),
        'category': category,
        'sub_category': sub_category,
        'title': title,
        'article': article,
        'applicability': applicability,
        'cross_numbers': cross_numbers,
        'image_links': image_links,
    }
