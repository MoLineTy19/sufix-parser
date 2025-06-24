from api.catalog.get_all_links import get_links_from_category
from api.catalog.get_categories_links import get_categories_links
from utils.get_page_content import get_page_content
from utils.get_url_from_save import get_url_from_save
from utils.is_exists_file import is_existing_save


def get_catalogs(save_result: bool = False) -> list:
    """
    Получение всех ссылок по категориям
    :param save_result: Сохранение результата
    :return: Список ссылок
    """
    # Существует ли файл со всеми категориями
    if not is_existing_save(file_path='categories_links.txt'):
        soup = get_page_content(url='https://sufix.pro')
        links = (get_categories_links(soup=soup, save_result=save_result)).get('links')

        result = []
        for url in links:
            print(url)
            link = get_links_from_category(url=url, save_result=save_result)
            result.append(link)
        return result

    # Существует ли файл со всеми ссылками из категорий
    if not is_existing_save(file_path='categories_all_links.txt'):
        links = get_url_from_save('categories_links.txt')

        result = []
        for url in links:
            print(url)
            link = get_links_from_category(url=url, save_result=save_result)
            result.append(link)
        return result

    # Если оба файла есть
    result = get_url_from_save('categories_all_links.txt')
    return result