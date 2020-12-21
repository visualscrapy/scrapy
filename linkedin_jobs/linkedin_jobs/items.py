import scrapy

class LinkedinJobsItem(scrapy.Item):
    job_position = scrapy.Field()
    job_company = scrapy.Field()
    job_location = scrapy.Field()
    job_last_update = scrapy.Field()
    loc = scrapy.Field()
