# -*- coding: utf-8 -*-
import datetime
import json
import time
import scrapy
from scrapy.crawler import CrawlerProcess

from children_1688.items import Children1688Item, SecondIndexItem, IndustrymarketdownItem
from children_1688.spiders.date_All_Year import getAllDayPerYear

'''
    - 陈航
    - 爬取三大指数昨日数据
    - 用法：scrapy crawl everyIndex --nolog 将类Children1688Pipeline中的w(写入)改为a+(追击) ，并且注释掉头列名
'''

class EveryindexSpider(scrapy.Spider):
    name = 'everyIndex'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.Children1688Pipeline': 300, }
    }

    def parse(self, response):
        data = response.xpath('//*[@id="main-chart-val"]/@value').extract_first()
        # data1 =     response.css('#main-chart-val::attr(value)').extract_first()
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract()
        category2 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[2]/p/a/text()').extract()
        # 去掉[] 以及''
        category1 = str(category1)[2:-2]
        category2 = str(category2)[2:-2]

        # 将数据转换为json，通过获取json数据的方式获取我们所需要的数据
        datajson = json.loads(data)  # dict
        purchaseIndex1688s = datajson["purchaseIndex1688"]["index"]["history"]
        purchaseIndexTbs = datajson['purchaseIndexTb']["index"]["history"]
        supplyIndexs = datajson['supplyIndex']["index"]["history"]
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        item = Children1688Item()
        item['category1'] = category1
        item['category2'] = category2
        item['showtime'] = yesterday
        item['purchaseIndex1688'] = purchaseIndex1688s[-1]
        item['purchaseIndexTb'] = purchaseIndexTbs[-1]
        item['supplyIndex'] = supplyIndexs[-1]
        item['crawl_Time'] = crawl_Time
        print(item)
        yield item

