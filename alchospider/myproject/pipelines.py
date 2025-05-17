# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

def parse_category(cat: dict) -> list[str]:
    if cat.get("parent"):
        return [cat["parent"]["name"], cat["name"]]
    return [cat["name"]]


def discount_percentage(current, previous) -> float:
    return round(100 * ((previous - current) / previous), 2)


class CreatePipeline:

    def process_item(self, pr, spider):
        item_dict = {
            "timestamp": datetime.datetime.now(datetime.UTC).timestamp(),
            # Дата и время сбора товара в формате timestamp.
            "RPC": pr['uuid'],  # Уникальный код товара.
            "url": pr["product_url"],  # Ссылка на страницу товара.
            "title": f"{pr['name']}, {pr['filter_labels'][0]['title']}",
            # Заголовок/название товара (! Если в карточке товара указан
            # цвет или объем, но их нет в названии, необходимо добавить их в title в формате:
            # "{Название}, {Цвет или Объем}").
            "marketing_tags": [p['title'] for p in pr.get("action_labels", [])],
            # Список маркетинговых тэгов, например: ['Популярный', 'Акция', 'Подарок'].
            # Если тэг представлен в виде изображения собирать его не нужно.
            "brand": pr["subname"],  # Бренд товара.
            "section": parse_category(pr['category']),
            # Иерархия разделов, например:
            # ['Игрушки', 'Развивающие и интерактивные игрушки', 'Интерактивные игрушки'].
            "price_data": {
                "current": float(pr['price']),
                # Цена со скидкой, если скидки нет то = original.
                "original": float(pr.get('prev_price')) if pr.get('prev_price') else float(
                    pr['price']
                ),  # Оригинальная цена.
                "sale_tag": f"Скидка {discount_percentage(
                    float(pr['price']),
                    float(pr['prev_price'])
                )}%" if pr.get(
                    'prev_price'
                ) else "Нет скидки"
                # Если есть скидка на товар то необходимо вычислить
                # процент скидки и записать формате: "Скидка {discount_percentage}%".
            },
            "stock": {
                "in_stock": pr['available'],  # Есть товар в наличии в магазине или нет.
                "count": pr['quantity_total']
                # Если есть возможность
                # получить информацию о количестве оставшегося товара в наличии, иначе 0.
            },
            "assets": {
                "main_image": pr["image_url"],  # Ссылка на основное изображение товара.
                "set_images": None,  # Список ссылок на все изображения товара.
                "view360": None,  # Список ссылок на изображения в формате 360.
                "video": None  # Список ссылок на видео/видеообложки товара.
            },
            "metadata": {
                "__description": "",  # Описание товара
                "slug": pr['slug'],
                "vendor_code": pr['vendor_code'],
                "filter_labels": pr['filter_labels'],
                # Также в metadata необходимо добавить все характеристики товара
                # которые могут быть на странице.
                # Например: Артикул, Код товара, Цвет, Объем, Страна производитель и т.д.
                # Где KEY - наименование характеристики.
            },
            "variants": 1,
            # Кол-во вариантов у товара в карточке
            # (За вариант считать только цвет или объем/масса.
            # Размер у одежды или обуви варинтами не считаются).
        }

        return item_dict
