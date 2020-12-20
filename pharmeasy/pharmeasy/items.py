import scrapy


class PharmeasyItem(scrapy.Item):
    product_id = scrapy.Field()
    product_name = scrapy.Field()
    product_manfacture = scrapy.Field()
    product_price = scrapy.Field()
    product_image_url = scrapy.Field()

