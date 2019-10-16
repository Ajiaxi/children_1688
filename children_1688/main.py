# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from children_1688.spiders.AttributeSegmentation1 import Attributesegmentation1Spider
from children_1688.spiders.AttributeSegmentation2 import Attributesegmentation2Spider
from children_1688.spiders.AttributeSegmentation3 import Attributesegmentation3Spider
from children_1688.spiders.AttributeSegmentation4 import Attributesegmentation4Spider
from children_1688.spiders.AttributeSegmentation5 import Attributesegmentation5Spider
from children_1688.spiders.AttributeSegmentationMiddle import AttributesegmentationSpider
from children_1688.spiders.AttributeSegmentationPrice import PriceSpider
from children_1688.spiders.BuyerSketch import BuyersketchSpider
from children_1688.spiders.IndustryMarketDown import IndustrymarketdownSpider
from children_1688.spiders.IndustryMarketDown1 import Industrymarketdown1Spider
from children_1688.spiders.IndustryMarketDown1_supply import Industrymarketdown1Spider_supply
from children_1688.spiders.IndustryMarketDown_supply import IndustrymarketdownSpider_supply
from children_1688.spiders.aliindex_30_2 import aliindex_30_2_spider
from children_1688.spiders.aliindex_30_hot import aliindex_30_hotSpider
from children_1688.spiders.aliindex_7_2 import aliindex_7_2_spider
from children_1688.spiders.aliindex_7_hot import aliindex_7_hotSpider
from children_1688.spiders.annualIndex import Children01Spider
from children_1688.spiders.annualIndex_supply import Children01Spider_supply
from children_1688.spiders.secondIndex import SecondindexSpider
from children_1688.spiders.secondIndex_supply import SecondindexSpider_supply
from children_1688.spiders.secondIndex_supply_update import SecondindexupdateSpider_supply
from children_1688.spiders.secondIndex_update import SecondindexupdateSpider

'''
    陈航
    增加顺序执行所有spider
    
    注： 如有相同spider名称
        需要改变相同的spider名称 
        
        localToHdfs    将 "/home/chenhang/chenhang"; 下的所有文件 push到103服务器上的hdfs系统中 路径为："/user/piday/zhili/chenhang";
        localToHive    将/home/chenhang/chenhang  下的所有文件 放到hive 中  关联hdfs路径为"/user/piday/zhili/chenhang"
        
'''
configure_logging()
runner = CrawlerRunner()

'''
    行业大盘
'''
flag = 'true'
# flag = 'false'

# if flag == 'true':
#     '''
#         采购商行业大盘 童装所有全年三大指数　二级目录指数　行业大盘热门行业
#         供应商行业大盘 童装所有全年三大指数　二级目录指数　行业大盘热门行业
#     '''
#     # runner.crawl(Children01Spider)
#     # runner.crawl(SecondindexupdateSpider)
#     runner.crawl(IndustrymarketdownSpider)

#     # runner.crawl(Children01Spider_supply)
#     # runner.crawl(SecondindexupdateSpider_supply)
#     runner.crawl(IndustrymarketdownSpider_supply)
# else:
#
#     '''
#         采购商行业大盘潜力行业 供应商行业大盘潜力行业
#     '''
#     runner.crawl(Industrymarketdown1Spider)
#     runner.crawl(Industrymarketdown1Spider_supply)


'''
    属性细分 热门基础属性5  热门营销属性1  价格带分布1
'''
runner.crawl(Attributesegmentation1Spider)
# runner.crawl(Attributesegmentation2Spider)
# runner.crawl(Attributesegmentation3Spider)
# runner.crawl(Attributesegmentation4Spider)
# runner.crawl(Attributesegmentation5Spider)

runner.crawl(AttributesegmentationSpider)

runner.crawl(PriceSpider)


'''
    采购商素描
'''
runner.crawl(BuyersketchSpider)

'''
    阿里排行 热搜榜和热销榜
'''

# runner.crawl(aliindex_7_2_spider)
# runner.crawl(aliindex_30_2_spider)
# runner.crawl(aliindex_7_hotSpider)
# runner.crawl(aliindex_30_hotSpider)


# 需要执行语句继续写runner.crawl(spider名称即可)

# 返回所有托管对象crawlers完成执行后触发的延迟。
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()  # 该脚本将在此处阻止，直到完成所有爬网作业
