# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class OlxItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    images_url = scrapy.Field()
