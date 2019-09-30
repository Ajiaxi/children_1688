import csv

class secondIndexPipelines(object):

    def __init__(self):
        # https://blog.csdn.net/lwgkzl/article/details/82147474  任务 明天早上测试是否可以追加数据 然后写整个页面的爬虫即可
        self.f = open("secondIndex.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['category1', 'category2', 'showtime', 'purchaseIndex1688', 'purchaseIndexTb', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['purchaseIndexTb'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()
