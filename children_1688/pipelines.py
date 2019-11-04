# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import datetime
import time

'''
    配置输出路径
'''
Children1688 = '/home/chenhang/zhili/craw/raw/hydp/cg/index/all/一级目录全年指数.csv'
Children1688Supply = '/home/chenhang/zhili/craw/raw/hydp/gy/index/all/一级目录全年指数.csv'
secondIndex = '/home/chenhang/zhili/craw/raw/hydp/cg/index/sub/二级目录全年指数.csv'
secondIndexSupply = '/home/chenhang/zhili/craw/raw/hydp/gy/index/sub/二级目录全年指数.csv'
IndustryMarketDown = '/home/chenhang/zhili/craw/raw/hydp/cg/rq/热门行业及潜力行业.csv'
IndustryMarketDownSupply = '/home/chenhang/zhili/craw/raw/hydp/gy/rq/热门行业及其潜力行业.csv'
Attributesegmentation = '/home/chenhang/zhili/craw/raw/attributes/base/属性细分热门基础属性.csv'
Attributesegmentation1 = '/home/chenhang/zhili/craw/raw/attributes/base/属性细分热门基础属性'
AttributesegmentationMiddle = '/home/chenhang/zhili/craw/raw/attributes/market/属性细分热门营销属性.csv'
AttributeSegmentationPrice = '/home/chenhang/zhili/craw/raw/attributes/price/属性细分价格带分布.csv'
BuyerSketch = '/home/chenhang/zhili/craw/raw/purchase/identify/采购商身份.csv'
aliIndex_7_1 = ''
aliIndex_7_2 = '/home/chenhang/zhili/craw/raw/alirank/search_7/搜索排行榜_7天_热搜榜.csv'
aliIndex_7_3 = ''
aliIndex_7_4 = ''
aliIndex_7_hot = '/home/chenhang/zhili/craw/raw/alirank/sale_7/热销榜_7.csv'
aliIndex_30_1 = ''
aliIndex_30_2 = '/home/chenhang/zhili/craw/raw/alirank/search_30/搜索排行榜_30天_热搜榜.csv'
aliIndex_30_3 = ''
aliIndex_30_4 = ''
aliIndex_30_hot = '/home/chenhang/zhili/craw/raw/alirank/sale_30/热销榜_30.csv'
aLiSupplyFileMain= '/home/chenhang/zhili/craw/raw/alisupply/main/阿里童装供应商信息_完整.csv'
aLiSupplyFileMarket = '/home/chenhang/zhili/craw/raw/alisupply/market/阿里童装供应商信息_主要市场.csv'
aLiSupplyFileProduct = '/home/chenhang/zhili/craw/raw/alisupply/product/阿里童装供应商信息_产品.csv'
Cmindexchild = '/home/chenhang/zhili/craw/raw/cmindex/child/4.csv'
Cmindexpricefabric = '/home/chenhang/zhili/craw/raw/cmindex/price/fabric/1.csv'
cmindexPriceGrey = '/home/chenhang/zhili/craw/raw/cmindex/price/grey/2.csv'
Cmindexsalefabric = '/home/chenhang/zhili/craw/raw/cmindex/sale/fabric/5.csv'
CmindexsaleGrey = '/home/chenhang/zhili/craw/raw/cmindex/sale/grey/6.csv'
'''
    获取上次更新时间　last_time_crawl
'''
csv_file = csv.reader(open(Children1688, 'r'))
content = []
for line in csv_file:
    content.append(line)
last_time_crawl = content[-1][-1].split(' ')[0]



class Children1688Pipeline(object):

    def __init__(self):
        # 1688采购商 全年写入
        # self.f = open(Children1688, "w")
        # 1688采购商 更新童装所有全年指数
        self.f = open(Children1688, "a+")
        self.writer = csv.writer(self.f)
        # self.writer.writerow(['目录1', '目录2', '展示时间', '1688采购指数', '淘宝采购指数', '1688供应指数' ,'爬取时间'])

    def process_item(self, item, spider):
        if datetime.datetime.strptime(item['showtime'], '%Y-%m-%d') >= datetime.datetime.strptime(last_time_crawl, '%Y-%m-%d'):
            list = [item['category1']+'\t'+ item['category2']+'\t'+item['showtime']+'\t'+str(item['purchaseIndex1688'])+'\t'+str(item['purchaseIndexTb'])+'\t'+str(item['supplyIndex'])+'\t'+item['crawl_Time']]
            self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class Children1688SupplyPipeline(object):

    def __init__(self):
        # 1688供应商 全年写入
        # self.f = open(Children1688Supply, "w")
        # 1688供应商 更新童装所有全年指数
        self.f = open(Children1688Supply, "a+")
        self.writer = csv.writer(self.f)
        # self.writer.writerow(['目录1', '目录2', '展示时间', '1688采购指数', '淘宝采购指数', '1688供应指数' ,'爬取时间'])

    def process_item(self, item, spider):
        if datetime.datetime.strptime(item['showtime'], '%Y-%m-%d') >= datetime.datetime.strptime(last_time_crawl,'%Y-%m-%d'):
            list = [item['category1']+'\t'+item['category2']+'\t'+item['showtime']+'\t'+str(item['purchaseIndex1688'])+'\t'+str(item['purchaseIndexTb'])+'\t'+str(item['supplyIndex'])+'\t'+item['crawl_Time']]
            self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class secondIndexPipelines(object):

    def __init__(self):
        self.f = open(secondIndex, "w")
        self.writer = csv.writer(self.f, delimiter='\t')
        self.writer.writerow(['目录1', '目录2', '展示时间', '1688采购指数', '1688供应指数', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'],item['category2'],item['showtime'],str(item['purchaseIndex1688']),str(item['supplyIndex']),item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class secondIndexupdatePipelines(object):
    def __init__(self):
        self.f = open(secondIndex, "a+")
        self.writer = csv.writer(self.f)

    def process_item(self, item, spider):
        if datetime.datetime.strptime(item['showtime'], '%Y-%m-%d') >= datetime.datetime.strptime(last_time_crawl,'%Y-%m-%d'):
            list = [item['category1']+'\t'+item['category2']+'\t'+item['showtime']+'\t'+str(item['purchaseIndex1688'])+'\t'+str(item['supplyIndex']),item['crawl_Time']]
            self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class secondIndexSupplyPipelines(object):

    def __init__(self):
        self.f = open(secondIndexSupply, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['目录1', '目录2', '展示时间', '1688采购指数', '1688供应指数', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1']+'\t'+item['category2']+'\t'+item['showtime']+'\t'+str(item['purchaseIndex1688'])+'\t'+str(item['supplyIndex'])+'\t'+
                item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class secondIndexupdateSupplyPipelines(object):

    def __init__(self):
        self.f = open(secondIndexSupply, "a+")
        self.writer = csv.writer(self.f)

    def process_item(self, item, spider):
        if datetime.datetime.strptime(item['showtime'], '%Y-%m-%d') >= datetime.datetime.strptime(last_time_crawl,'%Y-%m-%d'):
            list = [item['category1']+'\t'+item['category2']+'\t'+item['showtime']+'\t'+str(item['purchaseIndex1688'])+'\t'+str(item['supplyIndex'])+'\t'+
                    item['crawl_Time']]
            self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class IndustryMarketDownPipelines(object):
    def __init__(self):
        self.f = open(IndustryMarketDown, "w")
        self.writer = csv.writer(self.f,delimiter='\t')
        self.writer.writerow(['目录1', '目录2', '行业类型', '行业名称', '1688采购指数', '1688供应指数', '淘宝需求预测', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'],item['category2'],item['industry_Type'],item['industry_Name'],
                str(item['purchaseIndex1688']),str(item['supplyIndex']),item['demand_Forecast'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class IndustryMarketDownSupplyPipelines(object):
    def __init__(self):
        self.f = open(IndustryMarketDownSupply, "w")
        self.writer = csv.writer(self.f,delimiter='\t')
        self.writer.writerow(['目录1', '目录2', '行业类型', '行业名称', '1688采购指数', '1688供应指数', '淘宝需求预测', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'],item['category2'],item['industry_Type'],item['industry_Name'],
                str(item['purchaseIndex1688']),str(item['supplyIndex']),item['demand_Forecast'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class AttributesegmentationPipelines:
    def __init__(self):
        self.f = open(Attributesegmentation, "w")
        self.writer = csv.writer(self.f,delimiter='\t')
        self.writer.writerow(
            ['目录1', '目录2',  '行业类型','属性类型','属性名称', '1688采购指数','1688供应指数', '爬取时间'])
        # self.f.writelines(['目录1', '目录2',  '行业类型','属性类型','属性名称', '1688采购指数','1688供应指数', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1'] ,item['category2'] ,item['industry_Type'] ,item['attribute_Type'] ,
                item['attribute_Name'] ,item['purchaseIndex'] ,item['supplyIndex'] ,item['crawl_Time']]
        self.writer.writerow(list)
        # self.f.writelines(st)
        return item

    def close_spider(self, spider):  # 关闭

        self.f.close()

class AttributesegmentationMiddlePipelines:
    def __init__(self):
        self.f = open(AttributesegmentationMiddle, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '行业类型', '属性类型', '属性名称', '1688采购指数', '1688供应指数', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1']+'\t'+item['category2']+'\t'+item['industry_Type']+'\t'+item['attribute_Name']+'\t'+str(item['purchaseIndex'])
                +'\t'+str(item['supplyIndex'])+'\t'+item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class AttributeSegmentationPricePipelines:
    def __init__(self):
        self.f = open(AttributeSegmentationPrice, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '行业类型',  '属性名称1','价格分布1', '百分比',  '属性名称2','价格分布2', '百分比', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']+'\t'+
                item['index_Type']+'\t'+str(item['percentage'])+'\t'+item['attribute_Name1']+'\t'+item['index_Type1']+'\t'+str(item['percentage1'])+'\t'+item['crawl_Time']]
        self.writer.writerow(list)
        # return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class BuyerSketchPricePipelines:
    def __init__(self):
        self.f = open(BuyerSketch, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '行业类型',  '新老采购商', '百分比1', '非淘宝/淘宝店主', '百分比2', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']
                +'\t'+item['percentage']+'\t'+item['attribute_Name1'] +'\t'+item['percentage1']+'\t'+item['crawl_Time']]
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
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']+'\t'+
                item['search_Trend'] +'\t'+item['index']+'\t'+item['url']+'\t'+item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class aliIndex_7_2_Pipelines:
    def __init__(self):
        self.f = open(aliIndex_7_2, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名',  '关键词', '搜索指数', '全站商品数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']+'\t'+
                str(item['index']) +'\t'+str(item['total'])+'\t'+item['url']+'\t'+item['crawl_Time']]
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
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']+'\t'+item['rate'] +'\t'+item['total']+'\t'+item['url']+'\t'+item['crawl_Time']]
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
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']+'\t'+item['index'] +'\t'+item['total']+'\t'+item['url']+'\t'+item['crawl_Time']]
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
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']+'\t'+item['search_Trend'] +'\t'+item['index']+'\t'+item['url']+'\t'+item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_30_2_Pipelines:
    def __init__(self):
        self.f = open(aliIndex_30_2, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名',  '关键词', '搜索指数', '全站商品数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name'] +'\t'+str(item['index']) +'\t'+str(item['total'])+'\t'+item['url']+'\t'+item['crawl_Time']]
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
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']+'\t'+item['rate'] +'\t'+item['total']+'\t'+item['url']+'\t'+item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class aliIndex_30_4_Pipelines:
    def __init__(self):
        # self.f = open("/home/chenhang/workplace/crawlFile/阿里排行/搜索排行榜_30天_新词榜.csv", "w")
        self.f = open("搜索排行榜_30天_新词榜.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['目录1', '目录2', '榜名', '关键词', '搜索指数', '全站商品数', 'url', '爬取时间'])

    def process_item(self, item, spider):
        list = [item['category1']+'\t'+item['category2']+'\t'+item['attribute_Type']+'\t'+item['attribute_Name']+'\t'+str(item['index']) +'\t'+str(item['total'])+'\t'+item['url']+'\t'+item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_7_hot_Pipelines:
    def __init__(self):
        self.f = open(aliIndex_7_hot, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['name', 'type', 'title', 'price', 'trade'])

    def process_item(self, item, spider):
        list = [item['name']+'\t'+item['type']+'\t'+item['title']+'\t'+str(item['price'])+'\t'+str(item['trade'])]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aliIndex_30_hot_Pipelines:
    def __init__(self):
        self.f = open(aliIndex_30_hot, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['name', 'type', 'title', 'price', 'trade'])

    def process_item(self, item, spider):
        list = [item['name']+'\t'+item['type']+'\t'+item['title']+'\t'+str(item['price'])+'\t'+str(item['trade'])]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()

class aLiSupplyFileMain_pipelines:
    def __init__(self):
        self.f = open(aLiSupplyFileMain, "w")
        self.writer = csv.writer(self.f,delimiter='\t')
        self.writer.writerow(
            ['公司名', '地区', '主要产品', '主要市场', '交易量', '交易额', '爬取时间'])

    def process_item(self, item,spider):
        list = [item['companyName'],item['area'],item['mainProducts'],item['mainMarket'],item['tradingVolume'],item['transactionAmount'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self,spider):
        self.f.close()

class aLiSupplyFileMarket_pipelines:
    def __init__(self):
        self.f = open(aLiSupplyFileMarket, "w")
        self.writer = csv.writer(self.f,delimiter='\t')
        self.writer.writerow(
            ['公司名', '市场地区', '市场份额', '爬取时间'])

    def process_item(self, item,spider):
        list = [item['companyName'],item['area'],item['mainMarket'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self,spider):
        self.f.close()

class aLiSupplyFileProduct_pipelines:
    def __init__(self):
        self.f = open(aLiSupplyFileProduct, "w")
        self.writer = csv.writer(self.f,delimiter='\t')
        self.writer.writerow(
            ['公司名','产品', '爬取时间'])

    def process_item(self, item,spider):
        list = [item['companyName'],item['product'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self,spider):
        self.f.close()

class Cmindexchild_pipelines:
    def __init__(self):
        self.f = open(Cmindexchild, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['序号', '日期', '本期指数', '爬取时间'])

    def process_item(self, item,spider):
        list = [item['number']+'\t'+item['date']+'\t'+item['index']+'\t'+item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self,spider):
        self.f.close()

class Cmindexpricefabric_pipelines:
    def __init__(self):
        self.f = open(Cmindexpricefabric, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['期次', '指数', '涨跌幅', '爬取时间'])

    def process_item(self, item,spider):
        if datetime.datetime.strptime(item['date'], '%Y-%m-%d') >= datetime.datetime.strptime('2018-01-01', '%Y-%m-%d'):
            list = [item['date']+'\t'+item['index']+'\t'+item['index_hb']+'\t'+item['crawl_Time']]
            self.writer.writerow(list)
        return item

    def close_spider(self,spider):
        self.f.close()

class cmindexPriceGrey_pipelines:
    def __init__(self):
        self.f = open(cmindexPriceGrey, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['期次', '指数', '涨跌幅','爬取时间'])

    def process_item(self, item,spider):
        if datetime.datetime.strptime(item['date'], '%Y-%m-%d') >= datetime.datetime.strptime('2018-01-01', '%Y-%m-%d'):
            list = [item['date']+'\t'+item['index']+'\t'+item['index_hb']+'\t'+item['crawl_Time']]
            self.writer.writerow(list)
        return item

    def close_spider(self,spider):
        self.f.close()

class Cmindexsalefabric_pipelines:
    def __init__(self):
        self.f = open(Cmindexsalefabric, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['期次', '总景气指数', '涨跌幅', '流通景气指数', '生产景气指数', '爬取时间'])

    def process_item(self, item,spider):
        if datetime.datetime.strptime(item['round'], '%Y%m') >= datetime.datetime.strptime('201801', '%Y%m'):
            list = [item['round']+'\t'+item['index']+'\t'+item['index_hb']+'\t'+item['bindex1']+'\t'+item['bindex2']+'\t'+item['crawl_Time']]
            self.writer.writerow(list)
        return item

    def close_spider(self,spider):
        self.f.close()

class CmindexsaleGrey_pipelines:
    def __init__(self):
        self.f = open(CmindexsaleGrey, "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(
            ['期次', '总景气指数', '涨跌幅', '流通景气指数', '生产景气指数', '爬取时间'])

    def process_item(self, item,spider):
        if datetime.datetime.strptime(item['round'], '%Y%m') >= datetime.datetime.strptime('201801', '%Y%m'):
            list = [item['round']+'\t'+item['index']+'\t'+item['index_hb']+'\t'+item['bindex1']+'\t'+item['bindex2']+'\t'+item['crawl_Time']]
            self.writer.writerow(list)
        return item

    def close_spider(self,spider):
        self.f.close()
