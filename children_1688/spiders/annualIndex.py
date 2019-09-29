# -*- coding: utf-8 -*-
import json
import time

import scrapy

from children_1688.items import Children1688Item


class Children01Spider(scrapy.Spider):
    name = 'children_01'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311']

    def parse(self, response):
        data = response.xpath('//*[@id="main-chart-val"]/@value').extract_first()
        # data1 =     response.css('#main-chart-val::attr(value)').extract_first()
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract()
        category2 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[2]/p/a/text()').extract()
        # category1 = category1[1:-1]
        # category2 = category2[1:-1]
        showtime = '2018-9-28'
        line_Types = ['1688采购指数','淘宝采购指数','1688供应指数']

        datajson = json.loads(data)     #dict
        purchaseIndex1688s = datajson["purchaseIndex1688"]["index"]["history"]
        purchaseIndexTbs = datajson['purchaseIndexTb']["index"]["history"]
        supplyIndexs = datajson['supplyIndex']["index"]["history"]
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        print(len(purchaseIndex1688s))
        for i in range(0,len(purchaseIndex1688s)):
            item = Children1688Item()
            item['category1'] = category1
            item['category2'] = category2
            item['showtime'] = showtime
            item['line_Type'] = line_Types[0]
            item['value'] = purchaseIndex1688s[i]
            item['crawl_Time'] = crawl_Time

        # for i in range(0, len(purchaseIndexTbs)):
        #     item = Children1688Item()
        #     item['category1'] = category1
        #     item['category2'] = category2
        #     item['showtime'] = showtime
        #     item['line_Type'] = line_Types[1]
        #     item['crawl_Time'] = crawl_Time
        #
        # for i in range(0, len(supplyIndexs)):
        #     item = Children1688Item()
        #     item['category1'] = category1
        #     item['category2'] = category2
        #     item['showtime'] = showtime
        #     item['line_Type'] = line_Types[2]
        #     item['value'] = supplyIndexs[i]
        #     item['crawl_Time'] = crawl_Time

        yield item



