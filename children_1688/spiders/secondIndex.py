# -*- coding: utf-8 -*-
import datetime
import json
import time
import scrapy
from children_1688.items import SecondIndexItem
from children_1688.spiders.date_All_Year import getAllDayPerYear

'''
    - 陈航
    - 爬取我是采购商童装下的所有二级目录的1688采购指数和1688供应指数
    - 思路: 
            - 通过手动换网页网页爬取所需数据 
    - 用法: 
            - 控制台输入 scrapy crawl secondIndex --nolog 输入文件看pipelines中的类secondIndexPipelines 可改写文件路径
            - 注: 每执行一次需要换网址及其输入文件名称
    - 参数解析：
            - category1： 种类一 就是童装的意思
            - category2： 种类2 也就是童装下的二级目录
            - list_Count： 昨日去年到今日的所有日期
            - purchaseIndex1688s： 1688采购指数
            - supplyIndexs： 1688供应指数
            - crawl_Time： 爬取数据日期
    - bug残留：  9.30下午 5.12 mark,待修改为自动创建csv文件输入数据,修改为不用手动换网页和路径名
                10.5晚 解决
    - 状态： 32个类目都放在同一个csv中
'''

class SecondindexSpider(scrapy.Spider):
    name = 'secondIndex'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127424004']
    urls2 = [     'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127424004',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127496001',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1043351',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037003',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037039',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037012',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1048174',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122086001',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037011',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127430003',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127430004',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042754',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037004',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037649',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042841',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037010',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037006',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037007',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122704004',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,124188006',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,124196006',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122086002',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037005',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037192',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037648',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042840',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037008',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037009',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,126440003',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127164001',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122088001',
                  'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122698004']

    # next = ['127424004', '127496001', '1043351', '1037003', '1037039',
    #         '1037012', '1048174', '122086001', '1037011', '127430003',
    #         '127430004', '1042754', '1037004', '1037649', '1042841',
    #         '1037010', '1037006', '1037007', '122704004', '124188006',
    #         '124196006', '122086002', '1037005', '1037192', '1037648',
    #         '1042840', '1037008', '1037009', '126440003', '127164001',
    #         '122088001', '122698004']

    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.secondIndexPipelines': 300,},
    }

    def parse(self, response):

        data = response.xpath('//*[@id="main-chart-val"]/@value').extract_first()
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract()
        category2 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[2]/p/a/text()').extract()
        # 去掉[] 以及''
        category1 = str(category1)[2:-2]
        category2 = str(category2)[2:-2]
        datajson = json.loads(data)
        purchaseIndex1688s = datajson["purchaseIndex1688"]["index"]["history"]
        supplyIndexs = datajson['supplyIndex']["index"]["history"]
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # print(len(purchaseIndex1688s))
        print('正在爬取' + category2 + '网页,Please wait....')
        # 依次遍历，将数据添加进item中
        items = []
        for i in range(0, len(purchaseIndex1688s)):
        # debug时所用代码
        # for i in range(0,1):
            list_Count = self.datalist()
            item = SecondIndexItem()
            item['category1'] = category1
            item['category2'] = category2
            item['showtime'] = list_Count[i-1]
            item['purchaseIndex1688'] = purchaseIndex1688s[i]
            item['supplyIndex'] = supplyIndexs[i]
            item['crawl_Time'] = crawl_Time
            # yield item
            items.append(item)
        self.urls2.remove(response.url)
            # for i in range(0,len(self.urls2)):
        # for i in range(0,4):
        #     url = self.urls2[i]
        #     yield scrapy.Request(url=url, callback=self.parse)
        # https://stackoverflow.com/questions/6566322/scrapy-crawl-urls-in-order
        if self.urls2:
            r = scrapy.Request(url=self.urls2[0],callback=self.parse)
            items.append(r)
        # print(items)
        return items

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
        today = '20{}-{}-{}'.format(year, month, int(day) + 1)
        # 在2018年全年list列表里匹配，当大于去年昨日日期，则添加进新数组
        for x in range(0, len(data_2018)):
            if datetime.datetime.strptime(data_2018[x], '%Y-%m-%d') >= datetime.datetime.strptime(last_Year_Today,'%Y-%m-%d'):
                list_2018.append(data_2018[x])

        # 在2019年全年list列表里匹配，当今日日期大于列表元素时，添加进新数组
        for y in range(0, len(data_2019)):
            if datetime.datetime.strptime(today, '%Y-%m-%d') >= datetime.datetime.strptime(data_2019[y], '%Y-%m-%d'):
                list_2019.append(data_2019[y])
        # 去年昨日到今日的所有日期
        list_Count = list_2018 + list_2019
        # print(list_Count)
        return list_Count

