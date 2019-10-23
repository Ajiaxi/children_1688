# -*- coding: utf-8 -*-
import datetime
import json
import time
import scrapy
from children_1688.items import SecondIndexItem
from children_1688.spiders.date_All_Year import getAllDayPerYear

'''
    - 陈航
    - 爬取我是供应商童装下的所有二级目录的1688采购指数和1688供应指数
'''

class SecondindexupdateSpider_supply(scrapy.Spider):
    name = 'secondIndexupdate_supply'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=supplier&cat=311,127424004']
    next = ['127424004', '127496001', '1043351', '1037003', '1037039',
            '1037012', '1048174', '122086001', '1037011', '127430003',
            '127430004', '1042754', '1037004', '1037649', '1042841',
            '1037010', '1037006', '1037007', '122704004', '124188006',
            '124196006', '122086002', '1037005', '1037192', '1037648',
            '1042840', '1037008', '1037009', '126440003', '127164001',
            '122088001', '122698004']
    url = 'https://index.1688.com/alizs/market.htm?userType=supplier&cat=311,'
    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.secondIndexupdateSupplyPipelines': 300,},
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
        print('正在更新Spider secondIndexupdate_supply , 更新名称 :' + category2 + '网页,Please wait....')
        # 依次遍历，将数据添加进item中
        items = []
        for i in range(0, len(purchaseIndex1688s)):
        # debug时所用代码
        # for i in range(0,1):
            list_Count = self.datalist()
            item = SecondIndexItem()
            item['category1'] = category1
            item['category2'] = category2
            item['showtime'] = list_Count[i]
            item['purchaseIndex1688'] = purchaseIndex1688s[i]
            item['supplyIndex'] = supplyIndexs[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        if resurl == '127424004':
            print('正在更新Spider , 更新名称 : secondIndexupdate_supply 1688我是供应商网站行业大盘二级目录全年指数数据')
        self.next.remove(resurl)
        if self.next:
            r = scrapy.Request(url=self.url + self.next[0], callback=self.parse)
            items.append(r)
        elif len(self.next) == 0:
            print('更新Spider完成 , 更新数据名称 : secondIndexupdate_supply 1688我是供应商网站行业大盘二级目录全年指数数据')
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
        return list_Count