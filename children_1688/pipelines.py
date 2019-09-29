# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class Children1688Pipeline(object):
    def __init__(self):
        self.f = open("a.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['category1', 'category2', 'showtime', 'line_Type', 'value', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['line_Type'], item['value'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

