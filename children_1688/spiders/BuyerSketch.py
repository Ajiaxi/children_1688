# -*- coding: utf-8 -*-
import time

import scrapy

from children_1688.items import BuyerSketchItem

'''
    陈航
    用途：爬取采购商素描栏目 童装所有 
    数据很少直接手写
'''

class BuyersketchSpider(scrapy.Spider):
    name = 'BuyerSketch'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/purchaser.htm?userType=purchaser&cat=311']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.BuyerSketchPricePipelines': 300, },
    }

    def parse(self, response):
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract_first()
        category2 = '所有'
        attribute_Type = response.xpath('//*[@id="mod-identity"]/div[1]/h4/span/text()').extract()
        attribute_Name = ['新采购商','老采购商']
        percentage = ['64.53','35.47']
        attribute_Name1 = ['非淘宝店主','淘宝店主']
        percentage1 = ['47.81','52.19']
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items = []
        for i in range(0,len(attribute_Name)):
            item = BuyerSketchItem()
            item['category1'] = category1
            item['category2'] = category2
            item['attribute_Type'] = attribute_Type[0]
            item['attribute_Name'] = attribute_Name[i]
            item['percentage'] = percentage[i]
            item['attribute_Name1'] = attribute_Name1[i]
            item['percentage1'] = percentage1[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        print('更新Spider完成 , 更新数据名称 : BuyerSketch 1688网站采购商素描')
        return items