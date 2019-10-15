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
    
    
    注： 如有相同spider名称
        需要改变相同的spider名称 
        
        localToHdfs    将 "/home/chenhang/workplace/crawlfile"; 下的所有文件 push到103服务器上的hdfs系统中 路径为："/user/piday/zhili/chenhang";
        localToHive    将/home/chenhang/crawlfile   下的所有文件 放到hive 中  关联hdfs路径为"/user/piday/zhili/crawlfile"
        
'''
configure_logging()
runner = CrawlerRunner()


# 我是采购商全年三大指数
runner.crawl(Children01Spider)
# 采购商素描
runner.crawl(BuyersketchSpider)
# 需要执行语句继续写runner.crawl(spider名称即可)



# 返回所有托管对象crawlers完成执行后触发的延迟。
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until all crawling jobs are finished

