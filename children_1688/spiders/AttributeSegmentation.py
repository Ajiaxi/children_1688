# -*- coding: utf-8 -*-
import time

import scrapy

from children_1688.items import AttributesegmentationItem

'''
    用法：scrapy crawl AttributeSegmentation
    bug残留：10.5日晚，还是表结构问题，不清楚怎么去给item赋值，"童装,儿童防晒衣/皮肤衣,热门基础属性,"中性 : 3,570/2,795",2019-10-05 18:11:27" 差一个适用性别，不知如何插入
'''

class AttributesegmentationSpider(scrapy.Spider):
    name = 'AttributeSegmentation'
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
        'ITEM_PIPELINES' : {'children_1688.pipelines.AttributesegmentationPipelines': 300,}
    }
    def parse(self, response):

        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        attribute_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # attribute_Name1 = response.xpath('//ul[@class="tab-header fd-clr"]/li)').extract()
        attribute_Name = response.xpath('//ul[@class="property-list"]/li/p/text()').extract()
        purchase_supply1 = response.xpath('//li[@class="property fd-clr"]/div/p/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        items = []
        for i in range(0,len(attribute_Name)):
            # 热门基础属性采购和供应指数
            purchase_supply = str(attribute_Name[i])+' : '+purchase_supply1[i]+'/'+purchase_supply1[i+1]
            # print(purchase_supply)
            # str_line = str(category1)+','+str(category2[1])+','+str(attribute_Type[1])+','+str(attribute_Name1[0])+','+str(strline)+','+str(crawl_Time)
            str_line = str(category1)+','+str(category2[0])+','+str(attribute_Type[0])+','+str(purchase_supply)+','+str(crawl_Time)
            # print(str_line)
            item = AttributesegmentationItem()
            item['category1'] = category1
            item['category2'] = category2[0]
            item['attribute_Type'] = attribute_Type[0]
            item['purchase_supply'] = purchase_supply
            item['crawl_Time'] = crawl_Time
            items.append(item)
        print(str(response.url) + '爬取完成')
        self.urls2.remove(response.url)
        if self.urls2:
            print('正在爬取：'+str(self.urls2[0]))
            r = scrapy.Request(url=self.urls2[0],callback=self.parse)
            items.append(r)
        return items

