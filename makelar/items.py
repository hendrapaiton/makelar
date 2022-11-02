import scrapy


class MakelarItem(scrapy.Item):
    addr = scrapy.Field()
    port = scrapy.Field()
