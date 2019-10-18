# -*- coding: utf-8 -*-

import scrapy

'''
    爬取
    思路：
        获取所有数据后，在pipelines中判断　前一个公司名和下一个公司名是否相等，若相等，则将后公司名的编号改为２，否则不变还为１
'''
class aLiSupplyFileMainSpider(scrapy.Spider):
    name = 'alisupplyfilemain'
    allowed_domains = ['alibaba.com']
    start_urls = ['https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.9e19459b8XUEfx&viewType=L&n=50&indexArea=company_en&keyword=children_clothes&page=1&f1=y']
    head = 'https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.9e19459b8XUEfx&viewType=L&n=50&indexArea=company_en&keyword=children_clothes&page='
    end = '&f1=y'
    next = []
    for i in range(1, 51):
        next.append(i)

    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aLiSupplyFileMain_pipelines': 300, },
    }

    def parse(self, response):
        divs = response.xpath('//div[@class="item-main"]')
        companyNames = []
        numbers = 1
        areas = []
        mainProducts = []
        mainMarkets = []
        tradingVolumes = []
        transactionAmounts = []
        # 获取数据
        for div in divs:
            companyName = div.xpath('./div[1]/div[2]/div[1]/div[2]/h2/a/text()').extract()
            area = div.xpath().extract()
            mainProduct = div.xpath().extract()
            mainMarket = div.xpath().extract()
            tradingVolume = div.xpath().extract()
            transactionAmount = div.xpath().extract()

            companyNames.append(companyName[0])
            areas.append(area[0])
            mainProducts.append(mainProduct[0])
            mainMarkets.append(mainMarket[0])
            tradingVolumes.append(tradingVolume[0])
            transactionAmounts.append(transactionAmount[0])

        # 赋值数据
        for i in range(0,len(companyName)):
            pass


    '''
        companyName = scrapy.Field()
        number = scrapy.Field()
        area = scrapy.Field()
        mainProducts = scrapy.Field()
        mainMarket = scrapy.Field()
        tradingVolume = scrapy.Field()
        transactionAmount = scrapy.Field()
    '''