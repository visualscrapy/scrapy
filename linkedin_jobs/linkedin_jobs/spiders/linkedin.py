import scrapy
class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    page_num = 0
    def __init__(self, location='', page_num=page_num, **kwargs):
        self.start_urls = [f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?trk=public_jobs_jobs-search-bar_search-submit&location={location}&start={page_num}']
        super().__init__(**kwargs)
        self.location = location

    custom_settings = {"FEEDS": {"{}.csv".format(name + '__'): {"format": "csv"}}}

    def parse(self, response):
        self.page_num += 15
        for job in response.css('.result-card'):
            items = {
                'job_position': job.css('.job-result-card__title::text').extract(),
                'job_company': job.css('.job-result-card__subtitle-link::text').extract(),
                'job_location': job.css('.job-result-card__location::text').extract(),
                'job_last_update': job.css('time::attr(datetime)').extract(),
            }
            yield items
            start_urls = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?trk=public_jobs_jobs-search-bar_search-submit&&location={self.location}&start={self.page_num}'
        yield scrapy.Request(url=start_urls, callback=self.parse, dont_filter=True)
        print('=============================',start_urls)

# Runner scrapy crawl linkedin -a location=bangalore





    # class LinkedinSpider(scrapy.Spider):
    #     name = 'linkedin'
    #     page_num = 0
    #     start_urls = [
    #         f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/jobs-in-hyderabad?start={page_num}']
    #     custom_settings = {"FEEDS": {"{}.csv".format(name): {"format": "csv"}}}
    #     def parse(self, response):
    #         self.page_num += 15
    #         for job in response.css('.result-card'):
    #             job_position = job.css('.job-result-card__title::text').extract()
    #             job_company = job.css('.job-result-card__subtitle-link::text').extract()
    #             job_location = job.css('.job-result-card__location::text').extract()
    #             job_last_update = job.css('time::attr(datetime)').extract()
    #             items = {
    #                 'job_position': job_position,
    #                 'job_company': job_company,
    #                 'job_location': job_location,
    #                 'job_last_update': job_last_update,
    #             }
    #             yield items
    #         start_urls = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/jobs-in-hyderabad?start={self.page_num}'
    #         yield scrapy.Request(url=start_urls, callback=self.parse, dont_filter=True)
    #         print('----------------', start_urls)

