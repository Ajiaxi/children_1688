# -*- coding: utf-8 -*-
import time
import scrapy
from children_1688.items import IndustrymarketdownItem
from children_1688.logger import Logger

'''
    - 陈航
    - 爬取我是供应商行业大盘下面 最近30天儿童防晒衣/皮肤衣相关行业
    - 该数据为热门行业及其潜力行业.csv的第一种数据，在children_1688.pipelines.IndustryMarketDownSupplyPipelines中写入方式为w，并且有字段名写入
    
    - 用法: 控制台输入 scrapy crawl IndustryMarketDown_supply --nolog 输入文件看pipelines中的类IndustryMarketDown 可改写文件路径
'''

class IndustrymarketdownSpider_supply(scrapy.Spider):
    name = 'IndustryMarketDown_supply'
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
        'ITEM_PIPELINES' : {'children_1688.pipelines.IndustryMarketDownSupplyPipelines': 300,}
    }
    industry_Type = ['热门行业', '潜力行业']
    next2 = []

    def datadeal(self, category1, category2, industry_Name1, purchaseIndex16881, supplyIndex1, demand_Forecast1, divs,
                 items, industry_Type):
        # 拼接数据
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        list_industry_Name = []
        list_purchaseIndex1688 = []
        list_supplyIndex = []
        list_demand_Forecast = []
        category1 = str(category1)[2:-2]
        category2 = str(category2)[2:-2]
        industry_Name1 = str(industry_Name1)[2:-2]
        purchaseIndex16881 = str(purchaseIndex16881)[2:-2]
        purchaseIndex16881 = purchaseIndex16881.replace(',', '')
        supplyIndex1 = str(supplyIndex1)[2:-2]
        supplyIndex1 = supplyIndex1.replace(',', '')
        demand_Forecast1 = str(demand_Forecast1)[2:-2]
        list_industry_Name.append(industry_Name1)
        list_purchaseIndex1688.append(purchaseIndex16881)
        list_supplyIndex.append(supplyIndex1)
        list_demand_Forecast.append(demand_Forecast1)

        for div in divs:
            industry_Name2 = div.xpath('./div[1]/p[1]/@title').extract()
            purchaseIndex16882 = div.xpath('./div[1]/div[2]/p/text()').extract()
            supplyIndex2 = div.xpath('./div[1]/div[3]/p/text()').extract()
            demand_Forecast2 = div.xpath('./div/p[2]/text()').extract()
            industry_Name2 = str(industry_Name2)[2:-2]
            purchaseIndex16882 = str(purchaseIndex16882)[2:-2]
            purchaseIndex16882 = purchaseIndex16882.replace(',','')
            supplyIndex2 = str(supplyIndex2)[2:-2]
            supplyIndex2 = supplyIndex2.replace(',','')
            demand_Forecast2 = str(demand_Forecast2)[2:-2]
            list_industry_Name.append(industry_Name2)
            list_purchaseIndex1688.append(purchaseIndex16882)
            list_supplyIndex.append(supplyIndex2)
            list_demand_Forecast.append(demand_Forecast2)

        for i in range(0, len(list_supplyIndex)):
            item = IndustrymarketdownItem()
            item['category1'] = category1
            item['category2'] = category2
            item['industry_Type'] = industry_Type
            item['industry_Name'] = list_industry_Name[i]
            item['purchaseIndex1688'] = list_purchaseIndex1688[i]
            item['supplyIndex'] = list_supplyIndex[i]
            item['demand_Forecast'] = list_demand_Forecast[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        return items

    def parse(self, response):
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract()
        category2 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[2]/p/a/text()').extract()
        industry_Name1 = response.xpath('//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/p[1]/@title').extract()
        purchaseIndex16881 = response.xpath(
            '//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/div[2]/p/text()').extract()
        supplyIndex1 = response.xpath('//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/div[3]/p/text()').extract()
        demand_Forecast1 = response.xpath('//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/p[2]/text()').extract()
        divs = response.xpath('//*[@id="mod-related"]/div[2]/div[1]/div[1]/ul/li')
        items = []
        items = self.datadeal(category1, category2, industry_Name1, purchaseIndex16881, supplyIndex1, demand_Forecast1,
                              divs, items,
                              self.industry_Type[0])
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        self.next2.append(resurl)
        self.next.remove(resurl)
        if self.next:
            r = scrapy.Request(url=self.url + self.next[0], callback=self.parse)
            items.append(r)
        elif len(self.next) == 0:
            r = scrapy.Request(url=self.url + '127424004', dont_filter=True, callback=self.parse2)
            items.append(r)
        return items

    def parse2(self, response):
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract()
        category2 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[2]/p/a/text()').extract()
        industry_Name1 = response.xpath('//*[@id="mod-related"]/div[2]/div[2]/div[1]/div[2]/p[1]/@title').extract()
        purchaseIndex16881 = response.xpath(
            '//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/div[2]/p/text()').extract()
        supplyIndex1 = response.xpath('//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/div[3]/p/text()').extract()
        demand_Forecast1 = response.xpath('//*[@id="mod-related"]/div[2]/div[2]/div[1]/div[2]/p[2]/text()').extract()
        divs = response.xpath('//*[@id="mod-related"]/div[2]/div[2]/div[1]/ul/li')
        items = []
        items = self.datadeal(category1, category2, industry_Name1, purchaseIndex16881, supplyIndex1, demand_Forecast1,
                              divs, items,
                              self.industry_Type[1])
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        self.next2.remove(resurl)
        if self.next2:
            r = scrapy.Request(url=self.url + self.next2[0], dont_filter=True, callback=self.parse2)
            items.append(r)
        return items


