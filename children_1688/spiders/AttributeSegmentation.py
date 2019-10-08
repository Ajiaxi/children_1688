# -*- coding: utf-8 -*-
import time

import scrapy

from children_1688.items import AttributesegmentationItem

'''
    用法：scrapy crawl AttributeSegmentation
    bug残留：10.5日晚，还是表结构问题，不清楚怎么去给item赋值，"童装,儿童防晒衣/皮肤衣,热门基础属性,"中性 : 3,570/2,795",2019-10-05 18:11:27" 差一个适用性别，不知如何插入
            10.8日  写5个function 分别爬取适用性别 是否连帽 颜色等 然后装进items中 返回给pipelines 
            10.8日晚 尝试许久，发现请求urlpost只有25个，get15个，解决良久还是一筹莫展 已解决 但是发现list.remove(x): x not in list 留待将来
                最新解决办法还是写5个spider吧
'''

class AttributesegmentationSpider(scrapy.Spider):
    name = 'AttributeSegmentation'
    allowed_domains = ['1688.com']
    # start_urls = ['https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127424004']
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

    def start_requests(self):
        for url in self.urls2:
            yield scrapy.Request(url=url, method='POST', callback=self.parseApplicableGender)
    # 处理适用性别函数
    # def parseApplicableGender(self,response):
    def parseApplicableGender(self,response):
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
        for i in range(0, len(purchase_supply), 2):
            purchaseIndex.append(purchase_supply[i])
            supplyIndex.append(purchase_supply[i + 1])
        # 下列代码debug使用
        # print(purchaseIndex)
        # print(supplyIndex)
        # for i in range(0,len(supplyIndex)):
        #     print(str(category1)+str(category2[0])+str(industry_Type[1])+str(attribute_Type[0])+str(attribute_Name[i])+purchaseIndex[i]+str(purchaseIndex[i])+str(crawl_Time)+'\n')
        print('正在爬取：' + response.url)
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
            r = scrapy.Request(url=self.urls2[0], callback=self.parseApplicableGender)
            items.append(r)
        # print(items)
        return items
    # 是否连帽
    def parseWhetherHooded(self,response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 是否连帽等
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[2]/text()').extract()
        # 连帽 不连帽
        attribute_Name = response.xpath('//*[@id="tab-popular-base"]/div[2]/div[2]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[2]/div[1]/div/ul/li/div/p/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items = []
        purchaseIndex = []
        supplyIndex = []
        for i in range(0, len(purchase_supply), 2):
            purchaseIndex.append(purchase_supply[i])
            supplyIndex.append(purchase_supply[i + 1])
        print('正在爬取：' + str(self.urls2[0]))
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
        print(str(response.url) + '爬取完成')
        self.urls2.remove(response.url)
        print(items)
        if self.urls2:
            self.parse
            return items
    # 颜色
    def parseColour(self,response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 颜色
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[3]/text()').extract()
        # 白色 600 606 601 蕾丝
        attribute_Name = response.xpath('//*[@id="tab-popular-base"]/div[2]/div[3]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[3]/div[1]/div/ul/li/div/p/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items = []
        purchaseIndex = []
        supplyIndex = []
        for i in range(0, len(purchase_supply), 2):
            purchaseIndex.append(purchase_supply[i])
            supplyIndex.append(purchase_supply[i + 1])
        print('正在爬取：' + str(self.urls2[0]))
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
        print(str(response.url) + '爬取完成')
        self.urls2.remove(response.url)
        print(items)
        if self.urls2:
            self.parse
            return items
    # 上市年份季节
    def parseListedSeason(self,response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 上市年份季节
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[4]/text()').extract()
        # 2019年夏季 2019夏季 2019等
        attribute_Name = response.xpath('//*[@id="tab-popular-base"]/div[2]/div[4]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[4]/div[1]/div/ul/li/div/p/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items = []
        purchaseIndex = []
        supplyIndex = []
        for i in range(0, len(purchase_supply), 2):
            purchaseIndex.append(purchase_supply[i])
            supplyIndex.append(purchase_supply[i + 1])
        print('正在爬取：' + str(self.urls2[0]))
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
        print(str(response.url) + '爬取完成')
        self.urls2.remove(response.url)
        print(items)
        if self.urls2:
            self.parse
            return items
    # 品牌
    def parseBrand(self,response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 品牌
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[4]/text()').extract()
        # 洹彩 沃克森琦 等
        attribute_Name = response.xpath('//*[@id="tab-popular-base"]/div[2]/div[5]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[5]/div[1]/div/ul/li/div/p/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items = []
        purchaseIndex = []
        supplyIndex = []
        for i in range(0, len(purchase_supply), 2):
            purchaseIndex.append(purchase_supply[i])
            supplyIndex.append(purchase_supply[i + 1])
        print('正在爬取：' + str(self.urls2[0]))
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
        print(str(response.url) + '爬取完成')
        self.urls2.remove(response.url)
        print(items)
        if self.urls2:
            self.parse
            return items




    # def parse(self, response):
        # for i in range(0,32):
        # # 适用性别
        #     items1.append(self.parseApplicableGender(response))
        # print(items1)
        # 是否连帽
        items2 = self.parseWhetherHooded(response)
        # print(items2)
        # 颜色
        items3 = self.parseColour(response)
        # print(items3)
        # 上市年份季节
        items4 = self.parseListedSeason(response)
        # print(items4)
        # 品牌
        items5 = self.parseBrand(response)
        # print(items5)
        # for i in range(0,len(items1)):
        #     items.append(items1[i])
        # for i in range(0,len(items2)):
        #     items.append(items2[i])
        # for i in range(0,len(items3)):
        #     items.append(items3[i])
        # for i in range(0,len(items4)):
        #     items.append(items4[i])
        # for i in range(0,len(items5)):
        #     items.append(items5[i])
        #
        # yield items


