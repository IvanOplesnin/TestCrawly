# Alkoteka Spider (Scrapy)

## 📌 Описание
Этот проект реализует парсер интернет-магазина [alkoteka.com](https://alkoteka.com), используя фреймворк **Scrapy**. Парсер предназначен для сбора информации о товарах из выбранных категорий с учётом региональных данных (Краснодар) и возможностью использования прокси.

## 🔧 Особенности
- Получение данных из API сайта `alkoteka.com` по категориям
- Поддержка регионального фильтра (город: Краснодар) Указывается в url - "?city_uuid=4a70f9e0-46ae-11e7-83ff-00155d026416"
- Прокидывание бесплатных прокси в Middlware(прокси взяты с сайта https://ru.proxy-tools.com/proxy)
- Использование Pipeline для обработки входящего json

## 📁 Структура проекта
```
myproject/
├── myproject/
│   ├── spiders/
│   │   └── alkoteka_spider.py   # Основной паук
│   ├── pipelines.py            # Обработка данных
│   ├── middlewares.py          # Прокси Middleware
│   └── settings.py             # Настройки Scrapy
├── scrapy.cfg
└── README.md                   # Инструкция
```

## 📥 Установка
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Запуск парсера
```bash
cd alchospider
scrapy crawl alchospider -O result.json
```
Результат будет сохранён в файл `result.json` в формате JSON.

## ✅ Пример выходных данных
```json
{
  "timestamp": 1747495947.393847,
  "RPC": "002b0883-2be0-11e7-82c0-00155d026416",
  "url": "https://alkoteka.com/product/pivo-1/caringer-shvarc-bir_29294",
  "title": "Царингер Шварц Бир, 0.5 Л",
  "marketing_tags": [],
  "brand": "Zahringer Schwarz Bier",
  "section": [
    "Слабоалкогольные напитки",
    "Пиво"
  ],
  "price_data": {
    "current": 145.0,
    "original": 145.0,
    "sale_tag": "Нет скидки"
  },
  "stock": {
    "in_stock": true,
    "count": 422
  },
  "assets": {
    "main_image": "https://web.alkoteka.com/resize/350_500/product/2a/b7/29294_image.png",
    "set_images": null,
    "view360": null,
    "video": null
  },
  "metadata": {
    "__description": "",
    "slug": "caringer-shvarc-bir_29294",
    "vendor_code": 29294,
    "filter_labels": [
      {
        "title": "0.5 Л",
        "filter": "obem",
        "type": "range",
        "values": {
          "min": 0.5,
          "max": 0.5
        }
      },
      {
        "title": "Пиво",
        "filter": "categories",
        "type": "select",
        "value": "pivo"
      }
    ]
  },
  "variants": 1
}


```

## 🔐 Поддержка прокси
Проект использует список бесплатных HTTP-прокси (задано в `middlewares.py`).

## 📍 Регион
Параметр `city_uuid=4a70f9e0-46ae-11e7-83ff-00155d026416` установлен для города **Краснодар**. Задан в url.


---

> Автор тестового решения: Ivan Oplesnin
> Телеграмм: https://t.me/i_vanya0956
