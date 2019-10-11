# -*- coding: utf-8 -*-
import time

import scrapy

from children_1688.items import AttributeSegmentationMiddleItem

'''
    陈航
    爬取属性细分热门营销属性
    用法：scrapy crawl AttributeSegmentationMiddle
'''

class AttributesegmentationSpider(scrapy.Spider):
    name = 'AttributeSegmentationMiddle'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127424004']
    urls2 = ['https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127424004',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127496001',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1043351',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037003',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037039',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037012',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1048174',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,122086001',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037011',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127430003',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127430004',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1042754',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037004',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037649',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1042841',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037010',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037006',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037007',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,122704004',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,124188006',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,124196006',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,122086002',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037005',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037192',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037648',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1042840',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037008',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,1037009',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,126440003',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127164001',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,122088001',
             'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,122698004']
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
            # print(dict)
            attribute_Name.append(dict.get('attrValue'))
            purchaseIndex.append(dict.get('purchaseIndex'))
            supplyIndex.append(dict.get('saleOfferCount'))
        # 热门营销属性
        industry_Type = response.xpath('//*[@id="content"]/div/div[2]/div[3]/div[1]/h4/span/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items = []
        print('正在爬取......：' + response.url)
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
        print('爬取完成..........')
        self.urls2.remove(response.url)
        if self.urls2:
            r = scrapy.Request(url=self.urls2[0], callback=self.parse)
            items.append(r)
        # print(items)
        return items
