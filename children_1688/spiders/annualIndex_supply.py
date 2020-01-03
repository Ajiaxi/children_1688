# -*- coding: utf-8 -*-
import json
import time
import scrapy
from children_1688.items import Children1688Item
from children_1688.spiders.getLastYearTodayTtoToday import getDataList

'''
    - 陈航
    - 爬取我是供应商行业大盘儿童防晒衣/皮肤衣数据概况  三大指数去年昨日到今日一整年的数据
    - 用法: 控制台输入 scrapy crawl children_01_supply 输入文件看pipelines中的类Children1688Pipeline 可改写文件路径
'''

class Children01Spider_supply(scrapy.Spider):
    name = 'children_01_supply'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=supplier&cat=311']
    # 指定管道处理
    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.Children1688SupplyPipeline': 300,}
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
        datajson = json.loads(data)     #dict
        purchaseIndex1688s = datajson["purchaseIndex1688"]["index"]["history"]
        purchaseIndexTbs = datajson['purchaseIndexTb']["index"]["history"]
        supplyIndexs = datajson['supplyIndex']["index"]["history"]
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        print(len(purchaseIndex1688s))
        # 依次遍历，将数据添加进item中
        for i in range(0,len(purchaseIndex1688s)):
        # debug时所用代码
        # for i in range(0,1):
            list_Count = self.datalist()
            item = Children1688Item()
            item['category1'] = category1
            item['category2'] = category2
            print('正在爬取日期：'+str(list_Count[i]))
            item['showtime'] = list_Count[i]
            item['purchaseIndex1688'] = purchaseIndex1688s[i]
            item['purchaseIndexTb'] = purchaseIndexTbs[i]
            item['supplyIndex'] = supplyIndexs[i]
            item['crawl_Time'] = crawl_Time
            yield item

    def datalist(self):
        return getDataList()