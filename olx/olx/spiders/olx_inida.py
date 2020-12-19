import scrapy
import json
from scrapy.crawler import CrawlerProcess
import os
class OlxInidaSpider(scrapy.Spider):
    name = 'olx_inida'
    def __init__(self, category='', **kwargs):
        self.start_urls = [f'https://www.olx.in/api/relevance/v2/search?facet_limit=100&isSearchCall=true&lang=en&location=2007599&location_facet_limit=20&page=1&platform=web-desktop&spellcheck=true&user=1766179eac1x6afbaf98&query={category}']
        super().__init__(**kwargs)
    headers ={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    custom_settings = {"FEEDS":{"{}.csv".format(name):{"format":"csv"}}}

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0]+"&page="+str(1), headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        for offer in data['data']:
            items = {
                'title': offer['title'],
                'description': offer['description'].replace('\n',''),
                'price': offer['price']['value']['display'] if offer['price'] else '',
                'images_url': offer['images'][0]['url'],
                'location': offer['locations_resolved'].get('COUNTRY_name', '') +', '+
                            offer['locations_resolved'].get('ADMIN_LEVEL_1_name', '') +', '+
                            offer['locations_resolved'].get('ADMIN_LEVEL_3_name', '') +', '+
                            offer['locations_resolved'].get('SUBLOCALITY_LEVEL_1_name', ''),
            }
            yield items
        next_page = data['metadata'].get('next_page_url')
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        else:
            print('__________________till last page scrapped successfully....')

#main driver
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(OlxInidaSpider) #class name of the spider
    process.start()

#Runner:  scrapy crawl olx_inida -a category=apartment