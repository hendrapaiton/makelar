import scrapy

from makelar.items import MakelarItem


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['http://free-proxy-list.net/']

    def parse(self, response, **kwargs):
        items = MakelarItem()
        tr = response.xpath('//div[@class="table-responsive fpl-list"]/table/tbody/tr')
        for row in tr:
            items['addr'] = row.xpath('td/text()')[0].extract()
            items['port'] = row.xpath('td/text()')[1].extract()
            yield items
