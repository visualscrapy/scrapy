import scrapy
import re
import json
from ..items import JavascriptItem

class JavascriptLoadedSpider(scrapy.Spider):
    name = 'javascript_loaded'
    start_urls = ['https://quotes.toscrape.com/js/']
    # start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        items = JavascriptItem()
        data = re.findall("var data =(.+?);\n", response.body.decode("utf-8"), re.S)
        ls = []
        if data:
            ls = json.loads(data[0])
            for i in ls:
                title = i['text'],
                author = i['author']['name'],
                tags = i['tags']

                items['title'] = title
                items['author'] = author
                items['tags'] = tags
                yield items
                yield from response.follow_all(css='ul.pager a', callback=self.parse)
