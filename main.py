import logging

from api.catalog.get_catalog import get_catalogs
from api.page.get_page import get_page
from excel.save_data import save_data
from logger import setup_logging
from utils.download_image import download_image


def main() -> None:
    """Пример работы с API https://sufix.pro"""
    setup_logging()

    links = get_catalogs(save_result=True)
    len_links = len(links)
    logging.info(f"Обнаружено ссылок: {len_links}")

    for _, link in enumerate(links[:1], start=1):
        data = get_page(link)

        # Пример выходных данных
        updated_data = {
            'Артикул': data['article'],
            'Название': data['title'],
            'Категория': data['category'],
            'Подкатегория': data['sub_category'],
            'Ссылка': data['url'],
            'Применимость': data['applicability'] if data['applicability'] else '',
            'OEM': ';'.join(data['cross_numbers']) if data['cross_numbers'] else '' ,
            'Ссылки на изображения': ';'.join(data['image_links']) if data['image_links'] else '',
        }

        # Скачивание изображений
        for i, image_url in enumerate(data['image_links']):
            download_image(article=data['article'], url=image_url, index=i)

        logging.info(f'{_}/{len_links} Артикул: {updated_data['Артикул']}')
        save_data(updated_data)


if __name__ == '__main__':
    main()
