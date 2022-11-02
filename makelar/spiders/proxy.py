import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['http://free-proxy-list.net/']

    def parse(self, response):
        pass
