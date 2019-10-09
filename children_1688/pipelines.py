# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

from children_1688.items import Children1688Item, SecondIndexItem


class Children1688Pipeline(object):

    def __init__(self):
        # https://blog.csdn.net/lwgkzl/article/details/82147474  任务 明天早上测试是否可以追加数据 然后写整个页面的爬虫即可
        self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan/Top/annualIndex.csv", "a+")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['category1', 'category2', 'showtime', 'purchaseIndex1688', 'purchaseIndexTb', 'supplyIndex' ,'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['purchaseIndexTb'], item['supplyIndex'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class secondIndexPipelines(object):

    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan/Top/secondIndex.csv", "w")
        self.f = open("secondIndex.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['category1', 'category2', 'showtime', 'purchaseIndex1688', 'supplyIndex', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['supplyIndex'],
                item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class IndustryMarketDown(object):
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan/Down/IndustryMarketDown.csv", "w")
        # self.f = open("IndustryMarketDown.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['category1', 'category2', 'industry_Type', 'industry_Name', 'purchaseIndex1688', 'supplyIndex', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'], item['industry_Name'],
                item['purchaseIndex1688'], item['supplyIndex'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class IndustryMarketDown1(object):
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan/Down/IndustryMarketDown.csv", "a+")
        # self.f = open("IndustryMarketDown.csv", "a+")
        self.writer = csv.writer(self.f)

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'], item['industry_Name'],
                item['purchaseIndex1688'], item['supplyIndex'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class AttributesegmentationPipelines:
    def __init__(self):
        # self.f = open("Attributesegmentation.csv", "w")
        # self.f = open('/home/chenhang/workplace/crawlFile/Shuxingxifen', "w")
        # self.f = open('/home/chenhang/workplace/crawlFile/Shuxingxifen', "a+")
        self.f = open("Attributesegmentation.csv", "a+")
        self.writer = csv.writer(self.f)
        # self.writer.writerow(
        #     ['category1', 'category2',  'industry_Type','attribute_Type','attribute_Name', 'purchaseIndex','supplyIndex', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'],item['attribute_Type'],item['attribute_Name'],item['purchaseIndex'],item['supplyIndex'] ,item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class AttributesegmentationMiddlePipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/Shuxingxifen/AttributesegmentationMiddle.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['category1', 'category2',  'industry_Type','attribute_Name', 'purchaseIndex','supplyIndex', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'],item['attribute_Name'],item['purchaseIndex'],item['supplyIndex'] ,item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class AttributeSegmentationPricePipelines:
    def __init__(self):
        # self.f = open("/home/chenhang/workplace/crawlFile/Shuxingxifen/price.csv", "w")
        self.f = open("/home/chenhang/workplace/crawlFile/Shuxingxifen/price.csv", "a+")
        # self.f = open("price.csv", "w")
        self.writer = csv.writer(self.f)
        # self.writer.writerow(
        #     ['category1', 'category2', 'industry_Type',  'attribute_Name','index_Type', 'percentage',  'attribute_Name1','index_Type1', 'percentage1', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['index_Type'], item['percentage'],item['attribute_Name1'] ,item['index_Type1'], item['percentage1'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class BuyerSketchPricePipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/caigoushangsumiao/BuyerSketch.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['category1', 'category2', 'industry_Type',  'new/old', 'percentage', 'notaobao/taobao', 'percentage1', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] , item['percentage'],item['attribute_Name1'] , item['percentage1'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_7_1_Pipelines:
    def __init__(self):
        # 童装所有
        # self.f = open("/home/chenhang/workplace/crawlFile/aliindex/aliIndex_7_1.csv", "w")
        # 童装二级目录
        self.f = open("/home/chenhang/workplace/crawlFile/aliindex/aliIndex_7_1.csv", "a+")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['category1', 'category2', 'industry_Type',  'attribute_Name', 'search_Trend', 'index', 'url', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['search_Trend'] , item['index'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class aliIndex_7_2_Pipelines:
    def __init__(self):
        # self.f = open("/home/chenhang/workplace/crawlFile/aliindex/aliIndex_7_2.csv", "w")
        self.f = open("/home/chenhang/workplace/crawlFile/aliindex/aliIndex_7_2.csv", "a+")
        self.writer = csv.writer(self.f)
        # self.writer.writerow(
        #     ['category1', 'category2', 'industry_Type',  'attribute_Name', 'index', 'total', 'url', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['index'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_7_3_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/aliindex/aliIndex_7_3.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['category1', 'category2', 'industry_Type',  'attribute_Name', 'rate', 'total', 'url', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['rate'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class aliIndex_7_4_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/aliindex/aliIndex_7_4.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['category1', 'category2', 'industry_Type',  'attribute_Name', 'index', 'total', 'url', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['index'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()