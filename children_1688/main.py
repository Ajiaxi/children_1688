# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import os

# from children_1688.spiders.aliindex_30_4 import aliindex_30_4_spider
# from children_1688.spiders.annualIndex import Children01Spider
# from children_1688.spiders.AttributeSegmentation import AttributeSegmentationSpider
# from children_1688.spiders.annualIndexUpdate import annualIndexUpdateSpider
# from children_1688.spiders.annualIndexUpdateSupply import annualIndexUpdateSupplySpider
# from children_1688.spiders.AttributeSegmentationMiddle import AttributesegmentationMiddleSpider
# from children_1688.spiders.BuyerSketch import BuyersketchSpider
# from children_1688.spiders.IndustryMarketDown import IndustrymarketdownSpider
# from children_1688.spiders.IndustryMarketDown_supply import IndustrymarketdownSpider_supply
# from children_1688.spiders.aliindex_30_2 import aliindex_30_2_spider
# from children_1688.spiders.aliindex_30_hot import aliindex_30_hotSpider
# from children_1688.spiders.aliindex_7_2 import aliindex_7_2_spider
# from children_1688.spiders.aliindex_7_hot import aliindex_7_hotSpider
# from children_1688.spiders.secondIndex_supply_update import SecondindexupdateSpider_supply
# from children_1688.spiders.secondIndex_update import SecondindexupdateSpider
# from children_1688.spiders.AttributeSegmentationPrice import PriceSpider
from children_1688.spiders.alisupplyfilemaim import AlisupplyfilemainSpider

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor



'''
    陈航
    增加顺序执行所有spider
    
    注： 如有相同spider名称
        需要改变相同的spider名称 
        
        localToHdfs    将 "/home/chenhang/chenhang"; 下的所有文件 push到103服务器上的hdfs系统中 路径为："/user/piday/zhili/chenhang";
        localToHive    将/home/chenhang/chenhang  下的所有文件 放到hive 中  关联hdfs路径为"/user/piday/zhili/chenhang"
        
'''


# 设置没有任何日志输出。
configure_logging(install_root_handler=False)
# configure_logging()
runner = CrawlerRunner()

'''
    行业大盘
'''

'''
    采购商行业大盘 童装所有全年三大指数　二级目录指数　行业大盘热门行业/潜力行业
    
    供应商行业大盘 童装所有全年三大指数　二级目录指数　行业大盘热门行业/潜力行业
'''
# runner.crawl(annualIndexUpdateSpider)
# runner.crawl(SecondindexupdateSpider)
# runner.crawl(IndustrymarketdownSpider)
#
# runner.crawl(annualIndexUpdateSupplySpider)
# runner.crawl(SecondindexupdateSpider_supply)
# runner.crawl(IndustrymarketdownSpider_supply)
#
#
# '''
#     属性细分 热门基础属性  热门营销属性  价格带分布
# '''
# runner.crawl(AttributeSegmentationSpider)
# runner.crawl(AttributesegmentationMiddleSpider)
# runner.crawl(PriceSpider)
#
#
# '''
#     采购商素描
# '''
# runner.crawl(BuyersketchSpider)
#
#
# '''
#     阿里排行 热搜榜和热销榜
# '''
#
# runner.crawl(aliindex_7_2_spider)
# runner.crawl(aliindex_30_2_spider)
# runner.crawl(aliindex_7_hotSpider)
# runner.crawl(aliindex_30_hotSpider)
runner.crawl(AlisupplyfilemainSpider)

# 需要执行语句继续写runner.crawl(spider名称即可)

# 返回所有托管对象crawlers完成执行后触发的延迟。
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()  # 该脚本将在此处阻止，直到完成所有爬网作业
