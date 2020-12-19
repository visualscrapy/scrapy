# we are pass the city name on runner ==> scrapy crawl otm -a category=london
import scrapy
from ..items import OnthemarketItem

class OtmSpider(scrapy.Spider):
    name = 'otm'
    def __init__(self, category='', **kwargs):
        self.start_urls = [f'https://www.onthemarket.com/for-sale/property/{category}/']
        super().__init__(**kwargs)

    custom_settings = {"FEEDS":{"{}_london.csv".format(name):{"format":"csv"}}}

    def start_requests(self):
        # url = 'https://www.onthemarket.com/for-sale/property/london/'
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        items = OnthemarketItem()
        properties = response.css("li.result")
        for list in properties:
            items['price'] = list.css('.price-text >a ::text').extract_first()
            items['title'] = list.css('p >span.title>a::text').extract()
            items['address'] = list.css('.address >a::text').extract()
            items['description'] = list.css('.details > p.description::text').extract()
            items['contact'] = list.css('.marketed-by-contact >a:nth-child(1) >strong::text').extract()
            items['image_url'] = list.css('.media >* picture > img::attr(src)').extract()
            yield items
            yield from response.follow_all(css='li+ li a.arrow', callback=self.parse)


