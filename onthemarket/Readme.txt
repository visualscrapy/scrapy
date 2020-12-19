content-type: text/html; charset=UTF-8

#Runner: scrapy crawl otm -a category=london
# -a <== we use for parameter
# category <== variable
# london <== value
# relplace url=self.start_urls[0] with url =url
#if you dont want to pass category through CLI then disable __ini__()function
# items['price'] = list.css('.price-text >a ::text').get().encode('ascii', 'ignore').decode('utf-8').strip() # used for remove Euro symbol and etc.

it will added into settings.py file
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
