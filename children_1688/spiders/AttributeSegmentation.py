# -*- coding: utf-8 -*-
import time
import scrapy
from children_1688.items import AttributesegmentationItem

'''
    爬取属性细分热门基础属性 由5个parse合并成一个
    当请求重复url时,scrapy会自动过滤掉重复url,所以导致了我们的调用parse2parse3parse4parse5请求只能执行一次的情况
    解决办法在scrapy.Request中加上dont_filter=True
'''

class AttributeSegmentationSpider(scrapy.Spider):
    name = 'AttributeSegmentation'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,127424004']
    # next = ['127424004', '127496001', '1043351', '1037003']
    next = ['127424004', '127496001', '1043351', '1037003', '1037039',
            '1037012', '1048174', '122086001', '1037011', '127430003',
            '127430004', '1042754', '1037004', '1037649', '1042841',
            '1037010', '1037006', '1037007', '122704004', '124188006',
            '124196006', '122086002', '1037005', '1037192', '1037648',
            '1042840', '1037008', '1037009', '126440003', '127164001',
            '122088001', '122698004']
    url = 'https://index.1688.com/alizs/attr.htm?userType=purchaser&cat=311,'
    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.AttributesegmentationPipelines': 300,}
    }
    next2 = []
    next3 = []
    next4 = []
    next5 = []

    def datadeal(self,category1,category2,industry_Type,attribute_Type,attribute_Name,purchase_supply,items):
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        purchaseIndex = []
        dealpurchaseIndex = []
        supplyIndex = []
        dealsupplyIndex = []
        for i in range(0, len(purchase_supply), 2):
            purchaseIndex.append(purchase_supply[i])
            supplyIndex.append(purchase_supply[i + 1])
        for p in purchase_supply:
            if ',' in p :
                r = str(p).replace(',','')
                dealpurchaseIndex.append(r)
        for s in supplyIndex:
            if ',' in s:
                r = str(s).replace(',','')
                dealsupplyIndex.append(r)
        for i in range(0, len(attribute_Name)):
            item = AttributesegmentationItem()
            item['category1'] = category1
            item['category2'] = category2[0]
            item['industry_Type'] = industry_Type[0]
            item['attribute_Type'] = attribute_Type[0]
            item['attribute_Name'] = attribute_Name[i]
            item['purchaseIndex'] = dealpurchaseIndex[i]
            item['supplyIndex'] = dealsupplyIndex[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        return items

    # 处理适用性别函数
    def parse(self,response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 适用性别等
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[1]/text()').extract()
        # 中性 女性 男性 等
        attribute_Name = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[1]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[1]/div[1]/div/ul/li/div/p/text()').extract()
        items = []
        items = self.datadeal(category1,category2,industry_Type,attribute_Type,attribute_Name,purchase_supply,items)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        if resurl == '127424004':
            print('正在更新Spider　, 数据名称 : AttributeSegmentation 1688网站属性细分热门基础属性')
        self.next2.append(resurl)
        self.next.remove(resurl)
        if self.next:
            r = scrapy.Request(url=self.url+self.next[0], callback=self.parse)
            items.append(r)
        elif len(self.next) == 0:
            r = scrapy.Request(url=self.url+'127424004',callback=self.parse2)
            items.append(r)
        return items

    # 是否连帽
    def parse2(self, response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 是否连帽等
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[2]/text()').extract()
        # 连帽 不连帽
        attribute_Name = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[2]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[2]/div[1]/div/ul/li/div/p/text()').extract()
        items = []
        items = self.datadeal(category1, category2, industry_Type, attribute_Type, attribute_Name, purchase_supply,items)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        self.next3.append(resurl)
        self.next2.remove(resurl)
        if self.next2:
            r = scrapy.Request(url=self.url+self.next2[0], dont_filter=True, callback=self.parse2)
            items.append(r)
        elif len(self.next2) == 0:
            r = scrapy.Request(url=self.url + '127424004', dont_filter=True, callback=self.parse3)
            items.append(r)
        return items

    # 颜色
    def parse3(self, response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 颜色
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[3]/text()').extract()
        # 白色 600 606 601 蕾丝
        attribute_Name = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[3]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[3]/div[1]/div/ul/li/div/p/text()').extract()
        items = []
        items = self.datadeal(category1, category2, industry_Type, attribute_Type, attribute_Name, purchase_supply,
                              items)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        self.next4.append(resurl)
        self.next3.remove(resurl)
        if self.next3:
            r = scrapy.Request(url=self.url + self.next3[0], dont_filter=True, callback=self.parse3)
            items.append(r)
        elif len(self.next3) == 0:
            r = scrapy.Request(url=self.url+ '127424004', dont_filter=True, callback=self.parse4)
            items.append(r)
        return items

    # 上市年份季节
    def parse4(self, response):
        category1 = response.xpath('//div[contains(@class,"cate-first-level")]//a/text()').extract_first()
        category2 = response.xpath('//div[contains(@class,"cate-second-level")]//a/text()').extract()
        # 热门基础属性等
        industry_Type = response.xpath('//span[@class="ms-yh"]/text()').extract()
        # 上市年份季节
        attribute_Type = response.xpath('//*[@id="tab-popular-base"]/div[1]/div/ul/li[4]/text()').extract()
        # 2019年夏季 2019夏季 2019等
        attribute_Name = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[4]/div[1]/div/ul/li/p/@title').extract()
        purchase_supply = response.xpath(
            '//*[@id="tab-popular-base"]/div[2]/div[4]/div[1]/div/ul/li/div/p/text()').extract()
        items = []
        items = self.datadeal(category1, category2, industry_Type, attribute_Type, attribute_Name, purchase_supply,
                              items)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        self.next5.append(resurl)
        self.next4.remove(resurl)
        if self.next4:
            r = scrapy.Request(url=self.url + self.next4[0], dont_filter=True, callback=self.parse4)
            items.append(r)
        elif len(self.next4) == 0:
            r = scrapy.Request(url=self.url + '127424004', dont_filter=True, callback=self.parse5)
            items.append(r)
        return items

    # 品牌
    def parse5(self, response):
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
        items = []
        items = self.datadeal(category1, category2, industry_Type, attribute_Type, attribute_Name, purchase_supply,
                              items)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        self.next5.remove(resurl)
        if self.next5:
            r = scrapy.Request(url=self.url + self.next5[0], dont_filter=True, callback=self.parse5)
            items.append(r)
        elif len(self.next5) == 0:
            print('更新Spider完成 , 更新数据名称 : AttributeSegmentation 1688网站属性细分热门基础属性')
        return items