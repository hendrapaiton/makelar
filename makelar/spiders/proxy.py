import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['http://free-proxy-list.net/']

    def parse(self, response, **kwargs):
        tr = response.xpath('//div[@class="table-responsive fpl-list"]/table/tbody/tr')
        for row in tr:
            print("{}:{}".format(row.xpath('td/text()')[0].extract(), row.xpath('td/text()')[1].extract()))
