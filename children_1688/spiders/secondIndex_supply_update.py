# -*- coding: utf-8 -*-
import json
import time
import scrapy
from children_1688.items import SecondIndexItem
from children_1688.spiders.getLastYearTodayTtoToday import getDataList

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
        for i in range(0, len(purchaseIndex1688s)-1):
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
        self.next.remove(resurl)
        if self.next:
            r = scrapy.Request(url=self.url + self.next[0], callback=self.parse)
            items.append(r)
        return items

    def datalist(self):
        return getDataList()