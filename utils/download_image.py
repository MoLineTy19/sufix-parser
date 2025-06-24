import logging
import os

import requests
from PIL import Image


def process_image(image_path: str, output_path: str, target_ratio = (3, 4), target_resolution = (900, 1200)) -> None:
    img = Image.open(image_path)
    width, height = img.size
    current_ratio = width / height
    target_ratio_value = target_ratio[0] / target_ratio[1] # 3/4 = 0.75

    if current_ratio > target_ratio_value:
        # Слишком широкое: добавляем полосы сверху и снизу
        new_height = int(width / target_ratio_value)
        new_img = Image.new('RGB', (width, new_height), (255, 255, 255))
        offset = (0, (new_height - height) // 2)
        new_img.paste(img, offset)
    else:
        # Слишком высокое: добавляем полосы слева и справа
        new_width = int(height * target_ratio_value)
        new_img = Image.new('RGB', (new_width, height), (255, 255, 255))
        offset = ((new_width - width) // 2, 0)
        new_img.paste(img, offset)

    new_img = new_img.resize(target_resolution, Image.LANCZOS)
    new_img.save(output_path, quality=95)


def download_image(article: str, url: str, index: int, base_output_dir: str = 'images') -> None:
    """
    Скачивание изображение по ссылке
    :param article:
    :param url:
    :param index:
    :param base_output_dir:
    :return:
    """
    output_dir = os.path.join(base_output_dir, article)
    os.makedirs(output_dir, exist_ok=True)

    if index > 1:
        filename = f"{article} ({index}).png"
    else:
        filename = f"{article}.jpg"

    temp_path = os.path.join(output_dir, f"temp_{filename}")
    final_path = os.path.join(output_dir, filename)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Сохраняем временный файл
        with open(temp_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        # Обработка фотографии
        process_image(temp_path, final_path)

        # Удаляем временный файл
        os.remove(temp_path)

        logging.info(f'Скачано и обработано: {filename}')
    else:
        logging.info(f"Ошибка скачивания {url}: статус {response.status_code}")