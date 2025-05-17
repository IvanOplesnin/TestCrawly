import scrapy


class AlchospiderSpider(scrapy.Spider):
    name = "alchospider"
    start_urls = [
        "https://alkoteka.com/web-api/v1/product?city_uuid=4a70f9e0-46ae-11e7-83ff-00155d026416&page=1&per_page=100&root_category_slug=slaboalkogolnye-napitki-2",
        "https://alkoteka.com/web-api/v1/product?city_uuid=4a70f9e0-46ae-11e7-83ff-00155d026416&page=1&per_page=100&root_category_slug=krepkiy-alkogol",
        "https://alkoteka.com/web-api/v1/product?city_uuid=4a70f9e0-46ae-11e7-83ff-00155d026416&page=1&per_page=100&root_category_slug=vino"

    ]

    def parse(self, response, *args, **kwargs):
        result = response.json()

        for pr in result["results"]:
            self.log(f'Название напитка: {pr["name"]}')
            yield pr
