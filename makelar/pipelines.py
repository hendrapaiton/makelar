class MakelarPipeline:
    file = None

    def open_spider(self, spider):
        self.file = open('proxy.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write('{}:{}'.format(item['addr'], item['port']))
        return item
