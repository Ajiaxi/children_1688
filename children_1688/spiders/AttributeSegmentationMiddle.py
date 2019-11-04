# -*- coding: utf-8 -*-
import time

import scrapy
from children_1688.items import AttributeSegmentationMiddleItem

'''
    陈航
    爬取属性细分热门营销属性
    用法：scrapy crawl AttributeSegmentationMiddle
'''

class AttributesegmentationMiddleSpider(scrapy.Spider):
    name = 'AttributeSegmentationMiddle'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127424004']
    next = ['127424004', '127496001', '1043351', '1037003', '1037039',
            '1037012', '1048174', '122086001', '1037011', '127430003',
            '127430004', '1042754', '1037004', '1037649', '1042841',
            '1037010', '1037006', '1037007', '122704004', '124188006',
            '124196006', '122086002', '1037005', '1037192', '1037648',
            '1042840', '1037008', '1037009', '126440003', '127164001',
            '122088001', '122698004']
    url = 'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,'
    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.AttributesegmentationMiddlePipelines': 300,}
    }

    def parse(self,response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        data = response.xpath('//*[@id="bar-chart-val"]/@value').extract()
        for dic in data:
            dicts = eval(dic)
        attribute_Name = []
        purchaseIndex = []
        supplyIndex = []
        for dict in dicts:
            attribute_Name.append(dict.get('attrValue'))
            purchaseIndex.append(dict.get('purchaseIndex'))
            supplyIndex.append(dict.get('saleOfferCount'))
        # 热门营销属性
        industry_Type = response.xpath('//*[@id="content"]/div/div[2]/div[3]/div[1]/h4/span/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items = []
        for i in range(0, len(attribute_Name)):
            item = AttributeSegmentationMiddleItem()
            item['category1'] = category1
            item['category2'] = category2[0]
            item['industry_Type'] = industry_Type[0]
            item['attribute_Name'] = attribute_Name[i]
            item['purchaseIndex'] = purchaseIndex[i]
            item['supplyIndex'] = supplyIndex[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        if resurl == '127424004':
            print('正在更新Spider , 更新名称 : AttributeSegmentationMiddle 1688网站属性名称中部热门营销属性数据')
        self.next.remove(resurl)
        if self.next:
            r = scrapy.Request(url=self.url+self.next[0], callback=self.parse)
            items.append(r)
        elif len(self.next) == 0:
            print('更新Spider完成 , 更新名称 : AttributeSegmentationMiddle 1688网站属性名称中部热门营销属性数据')
        return items
