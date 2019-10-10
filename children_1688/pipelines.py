# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class Children1688Pipeline(object):

    def __init__(self):
        # 1688采购商 全年写入
        self.f = open("/home/chenhang/workplace/crawlFile/行业大盘-我是采购商/行业大盘上部/一级目录全年指数.csv", "w")
        # 1688采购商 每天的index写入 spider为everyIndex
        # self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan/Top/annualIndex.csv", "a+")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['目录1', '目录2', '展示时间', '1688采购指数', '淘宝采购指数', '1688供应指数' ,'爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['purchaseIndexTb'], item['supplyIndex'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class Children1688SupplyPipeline(object):

    def __init__(self):
        # 1688供应商 全年写入
        self.f = open("/home/chenhang/workplace/crawlFile/行业大盘-我是供应商/行业大盘上部/一级目录全年指数", "w")
        # 1688供应商 每天的index写入 spider为everyIndex
        # self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan_Supply/Top/annualIndex.csv", "a+")

        self.writer = csv.writer(self.f)
        self.writer.writerow(['目录1', '目录2', '展示时间', '1688采购指数', '淘宝采购指数', '1688供应指数' ,'爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['purchaseIndexTb'], item['supplyIndex'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class secondIndexPipelines(object):

    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/行业大盘-我是采购商/行业大盘上部/二级目录全年指数.csv", "w")
        # self.f = open("secondIndex.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['目录1', '目录2', '展示时间', '1688采购指数', '1688供应指数', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['supplyIndex'],
                item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class secondIndexSupplyPipelines(object):

    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/行业大盘-我是供应商/行业大盘上部/二级目录全年指数.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['目录1', '目录2', '展示时间', '1688采购指数', '1688供应指数', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['supplyIndex'],
                item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class IndustryMarketDown(object):
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/行业大盘-我是采购商/行业大盘下部/热门行业及其潜力行业.csv", "w")
        # self.f = open("IndustryMarketDown.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['目录1', '目录2', '行业类型', '行业名称', '1688采购指数', '1688供应指数', '淘宝需求预测', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'], item['industry_Name'],
                item['purchaseIndex1688'], item['supplyIndex'], item['demand_Forecast'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class IndustryMarketDowntest(object):
    def __init__(self):
        # self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan/Down/IndustryMarketDown.csv", "w")
        self.f = open("IndustryMarketDown.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['目录1', '目录2', '行业类型', '行业名称', '1688采购指数', '1688供应指数', '淘宝需求预测', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'], item['industry_Name'],
                item['purchaseIndex1688'], item['supplyIndex'], item['demand_Forecast'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class IndustryMarketDownSupplyPipelines(object):
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/行业大盘-我是供应商/行业大盘下部/热门行业及其潜力行业.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['目录1', '目录2', '行业类型', '行业名称', '1688采购指数', '1688供应指数', '淘宝需求预测', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'], item['industry_Name'],
                item['purchaseIndex1688'], item['supplyIndex'], item['demand_Forecast'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class IndustryMarketDown1(object):
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/行业大盘-我是采购商/行业大盘下部/热门行业及其潜力行业.csv", "a+")
        self.writer = csv.writer(self.f)

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'], item['industry_Name'],
                item['purchaseIndex1688'], item['supplyIndex'], item['demand_Forecast'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class IndustryMarketDown1SupplyPipelines(object):
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/行业大盘-我是供应商/行业大盘下部/热门行业及其潜力行业.csv", "a+")
        self.writer = csv.writer(self.f)

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'], item['industry_Name'],
                item['purchaseIndex1688'], item['supplyIndex'], item['demand_Forecast'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class AttributesegmentationPipelines:
    def __init__(self):
        self.f = open('/home/chenhang/workplace/crawlFile/属性细分/属性细分热门基础属性.csv', "w")
        # self.f = open('/home/chenhang/workplace/crawlFile/属性细分/属性细分热门营销属性.csv', "a+")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2',  '行业类型','属性类型','属性名称', '1688采购指数','1688供应指数', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'],item['attribute_Type'],item['attribute_Name'],item['purchaseIndex'],item['supplyIndex'] ,item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class AttributesegmentationMiddlePipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/属性细分/属性细分热门营销属性.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '行业类型', '属性类型', '属性名称', '1688采购指数', '1688供应指数', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'],item['attribute_Name'],item['purchaseIndex'],item['supplyIndex'] ,item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class AttributeSegmentationPricePipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/属性细分/属性细分价格带分布.csv", "w")
        # self.f = open("/home/chenhang/workplace/crawlFile/Shuxingxifen/price.csv", "a+")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '行业类型',  '属性名称1','价格分布1', '百分比',  '属性名称2','价格分布2', '百分比', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['index_Type'], item['percentage'],item['attribute_Name1'] ,item['index_Type1'], item['percentage1'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class BuyerSketchPricePipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/采购商素描/采购商身份.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '行业类型',  '新老采购商', '百分比1', '非淘宝/淘宝店主', '百分比2', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] , item['percentage'],item['attribute_Name1'] , item['percentage1'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_7_1_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_7天_上升榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名',  '关键词', '搜索趋势', '搜索指数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['search_Trend'] , item['index'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class aliIndex_7_2_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_7天_热搜榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名',  '关键词', '搜索指数', '全站商品数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['index'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_7_3_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_7天_转化率榜榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名',  '关键词', '搜索转化率', '全站商品数', 'url', '爬取时间'])
    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['rate'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class aliIndex_7_4_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_7天_新词榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名', '关键词', '搜索指数', '全站商品数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['index'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_30_1_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_30天_上升榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名', '关键词', '搜索趋势', '搜索指数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['search_Trend'] , item['index'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_30_2_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_30天_热搜榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名',  '关键词', '搜索指数', '全站商品数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['index'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class aliIndex_30_3_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_30天_转化率榜榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名', '关键词', '搜索转化率', '全站商品数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['rate'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class aliIndex_30_4_Pipelines:
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_30天_新词榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名', '关键词', '搜索指数', '全站商品数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['attribute_Type'],item['attribute_Name'] ,item['index'] , item['total'],item['url'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()