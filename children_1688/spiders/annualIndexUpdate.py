# -*- coding: utf-8 -*-
import datetime
import json
import time
import scrapy

from children_1688.items import Children1688Item
from children_1688.spiders.date_All_Year import getAllDayPerYear

'''
    - 陈航
    - 爬取我是采购商三大指数昨日数据
    - 用法：scrapy crawl everyIndex --nolog 将类Children1688Pipeline中的w(写入)改为a+(追击) ，并且注释掉头列名
'''

class annualIndexUpdateSpider(scrapy.Spider):
    name = 'everyIndex'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.Children1688Pipeline': 300, }
    }

    def parse(self, response):
        print('正在更新Spider..... , 更新数据名称 : 1688我是采购商网站行业大盘童装所有全年三大指数')
        data = response.xpath('//*[@id="main-chart-val"]/@value').extract_first()
        # data1 =     response.css('#main-chart-val::attr(value)').extract_first()
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract()
        category2 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[2]/p/a/text()').extract()
        # 去掉[] 以及''
        category1 = category1[0]
        category2 = category2[0]
        # 将数据转换为json，通过获取json数据的方式获取我们所需要的数据
        datajson = json.loads(data)     #dict
        purchaseIndex1688s = datajson["purchaseIndex1688"]["index"]["history"]
        purchaseIndexTbs = datajson['purchaseIndexTb']["index"]["history"]
        supplyIndexs = datajson['supplyIndex']["index"]["history"]
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # 依次遍历，将数据添加进item中
        for i in range(0,len(purchaseIndex1688s)):
        # debug时所用代码
        # for i in range(0,1):
            list_Count = self.datalist()
            item = Children1688Item()
            item['category1'] = category1
            item['category2'] = category2
            print('everyIndex 正在爬取日期：'+str(list_Count[i]))
            item['showtime'] = list_Count[i]
            item['purchaseIndex1688'] = purchaseIndex1688s[i]
            item['purchaseIndexTb'] = purchaseIndexTbs[i]
            item['supplyIndex'] = supplyIndexs[i]
            item['crawl_Time'] = crawl_Time
            yield item
        print('更新Spider完成 , 更新数据名称 : everyIndex 1688我是采购商商网站行业大盘童装所有全年三大指数')

    def datalist(self):
        # 获取2018年全年的日期
        data_2018 = getAllDayPerYear(2018)
        # 获取2019年全年的日期
        data_2019 = getAllDayPerYear(2019)
        list_2018 = []
        list_2019 = []
        year = time.strftime('%y', time.localtime(time.time()))
        month = time.strftime('%m', time.localtime(time.time()))
        day = int(time.strftime('%d', time.localtime(time.time()))) - 1
        # 获取去年昨日的日期 添加20原因：结果会显示为18-1-1 没有20
        last_Year_Today = '20{}-{}-{}'.format(int(year) - 1, month, day)
        # 获取今日的日期
        today = '20{}-{}-{}'.format(year, month, int(day)+1)
        # 在2018年全年list列表里匹配，当大于去年昨日日期，则添加进新数组
        for x in range(0, len(data_2018)):
            if datetime.datetime.strptime(data_2018[x],'%Y-%m-%d') >= datetime.datetime.strptime(last_Year_Today,'%Y-%m-%d'):
                list_2018.append(data_2018[x])
        # 在2019年全年list列表里匹配，当今日日期大于列表元素时，添加进新数组
        for y in range(0, len(data_2019)):
            if datetime.datetime.strptime(today,'%Y-%m-%d') >= datetime.datetime.strptime(data_2019[y],'%Y-%m-%d'):
                list_2019.append(data_2019[y])
        # 去年昨日到今日的所有日期
        list_Count = list_2018 + list_2019
        return list_Count