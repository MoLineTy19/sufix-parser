def get_url_from_save(file_path: str) -> list:
    """
    Получает ссылки из файла
    :param file_path: Путь до файла
    :return: Список ссылок
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        categories_links = f.readlines()
    return categories_links