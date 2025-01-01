import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime

class GilbertSpider(CrawlSpider):
    name = "gilbert"
    allowed_domains = ["www.wikiart.org"]
    start_urls = ["https://www.wikiart.org/en/gilbert-stuart/all-works"]

    rules = [
        Rule(
            link_extractor=LinkExtractor(allow=r"/gilbert-stuart/"),
            callback="parse_item",
            follow=True,
            process_request="enable_impersonate",
        ),
    ]

    def enable_impersonate(self, request, response):
        request.meta["impersonate"] = "chrome110"
        return request


    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
            "https": "scrapy_impersonate.ImpersonateDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }
    
    def start_requests(self):
        for url in self.start_urls:
            for browser in ["chrome110", "edge99", "safari15_5"]:
                self.logger.info(f"Requesting {url} with browser: {browser}")
                yield scrapy.Request(
                    url,
                    dont_filter=True,
                    meta={"impersonate": browser},
                )


    def parse_item(self, response):

        title = response.xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/main[1]/div[2]/article[1]/h3[1]/text()").get()
        date = response.xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/main[1]/div[2]/article[1]/ul[1]/li[1]/span[1]/text()").get() 
        media = response.xpath("//li[4]/span[1]/a/text()").getall() 
        location = response.xpath("//li[5]/span[1]/text()").get()  
        url = response.url
        image_urls =  response.xpath("//main[1]/div[2]/aside[1]/div[1]/img[1]/@src").get()
        dimensions = response.xpath("//li[s[@class='title' and text()='Dimensions:']]/text()").getall()
        scraped_at = datetime.datetime.now().strftime("%d %B %Y")

        if title is not None or title != "":
             yield {
            "title": title,
            "date": date,
            "media": media,
            "location": location,
            "url": url,
            "image_urls": image_urls,
            "dimensions": dimensions,
            "scraped_at": scraped_at,
             }
        else:
           pass

       
