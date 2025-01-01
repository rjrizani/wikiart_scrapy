# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiartItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    media = scrapy.Field()
    location = scrapy.Field()
    image_urls = scrapy.Field()
    url = scrapy.Field()
    dimensions = scrapy.Field()
    scraped_at = scrapy.Field()
    

