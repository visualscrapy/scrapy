import scrapy
import json
from ..items import PharmeasyItem

class PeasySpider(scrapy.Spider):
    name = 'peasy'
    custom_settings = {"FEEDS":{"{}.csv".format(name):{"format":"csv"}}}
    page_num =1
    def start_requests(self):
        global page_num
        base_url = 'https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=87&page={}'.format(self.page_num)
        yield scrapy.Request(url=base_url, callback=self.parse)

    def parse(self, response):
        self.page_num+=1
        items = PharmeasyItem()
        data = json.loads(response.text)
        if data['data']['products']:
            for product in data['data']['products']:
                items = {
                    'product_id': product['productId'],
                    'product_name': product['name'] ,
                    'product_manfacture': product['manufacturer'],
                    'product_price': product['salePriceDecimal'],
                    'product_image_url': product['images'][0] if product['images'] else '',
                    'product_available': product['isAvailable'],
                }
                yield items
            url='https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=87&page={}'.format(self.page_num)
            yield scrapy.Request(url=url, callback=self.parse)
            print('----------------',url)




