# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from children_1688.spiders.BuyerSketch import BuyersketchSpider
from children_1688.spiders.annualIndex import Children01Spider

'''
    陈航
    增加顺序执行所有spider

'''
configure_logging()
runner = CrawlerRunner()

'''
    注： 如有相同spider名称
        需要改变相同的spider名称 
'''

# 我是采购商全年三大指数
runner.crawl(Children01Spider)
# 采购商素描
runner.crawl(BuyersketchSpider)
# 需要执行语句继续写runner.crawl(spider名称即可)



# 返回所有托管对象crawlers完成执行后触发的延迟。
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until all crawling jobs are finished




# os.system('scrapy crawl aliindex_30_3 -s CLOSESPIDER_TIMEOUT=300')
# os.system('aliindex_30_3爬取完成******************************************************')
# os.system('scrapy crawl aliindex_30_4 -s CLOSESPIDER_TIMEOUT=300')
# os.system('aliindex_30_4爬取完成******************************************************')
