# -*- coding: utf-8 -*-
import time
import scrapy
from children_1688.items import AttributesegmentationItem


class AttributesegmentationSpider(scrapy.Spider):
    name = 'AttributeSegmentation1'
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

    # 处理适用性别函数
    def parse(self,response):
        # print('开始爬虫')
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 适用性别等
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[1]/text()').extract()
        # 中性 女性 男性 等
        attribute_Name = response.xpath('//*[@id="tab-popular-base"]/div[2]/div[1]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath('//*[@id="tab-popular-base"]/div[2]/div[1]/div[1]/div/ul/li/div/p/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items = []
        purchaseIndex = []
        supplyIndex = []
        print('正在爬取' + str(category2[0]) + '网页,Please wait....')
        for i in range(0, len(purchase_supply), 2):
            purchaseIndex.append(purchase_supply[i])
            supplyIndex.append(purchase_supply[i + 1])
        for i in range(0, len(attribute_Name)):
            item = AttributesegmentationItem()
            item['category1'] = category1
            item['category2'] = category2[0]
            item['industry_Type'] = industry_Type[0]
            item['attribute_Type'] = attribute_Type[0]
            item['attribute_Name'] = attribute_Name[i]
            item['purchaseIndex'] = purchaseIndex[i]
            item['supplyIndex'] = supplyIndex[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        self.urls2.remove(response.url)
        if self.urls2:
            r = scrapy.Request(url=self.urls2[0], callback=self.parse)
            items.append(r)
        return items
