import os


def is_existing_save(file_path: str) -> bool:
    """
    Проверка на существующий файл со ссылками
    :param file_path: Путь до файла
    :return: Существующий ли файл
    """

    if os.path.exists(file_path):
        return True
    else:
        return False