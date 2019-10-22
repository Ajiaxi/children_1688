# -*- coding: utf-8 -*-
import scrapy

from children_1688.items import aLiSupplyFileMain_Item

'''
    爬取
    思路：
        获取所有数据后，在pipelines中判断　前一个公司名和下一个公司名是否相等，若相等，则将后公司名的编号改为２，否则不变还为１
'''
class AlisupplyfilemainSpider(scrapy.Spider):
    name = 'alisupplyfilemain'
    allowed_domains = ['alibaba.com']
    # start_urls = ['https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.9e19459b8XUEfx&viewType=L&n=50&indexArea=company_en&keyword=children_clothes&page=1&f1=y']
    start_urls = ['https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.1f86459bWExbQ1&n=38&f1=y&indexArea=company_en&viewType=L&keyword=children_clothes&page=1']
    # head = 'https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.9e19459b8XUEfx&viewType=L&n=50&indexArea=company_en&keyword=children_clothes&page='
    head = 'https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.1f86459bWExbQ1&n=38&f1=y&indexArea=company_en&viewType=L&keyword=children_clothes&page='
    # end = '&f1=y'
    next = []
    for i in range(1,58):
        next.append(str(i))
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aLiSupplyFileMain_pipelines': 300, },
    }

    def parse(self, response):
        divs = response.xpath('.//div[@class="item-main"]')
        companyNames = []
        numbers = 1
        areas = []
        mainProducts = []
        mainMarkets = []
        tradingVolumes = []
        transactionAmounts = []
        items = []
        # 获取数据
        for div in divs:
            companyName = div.xpath('div[1]/div[2]/div[1]/div[2]/h2/a/text()').extract()
            if len(companyName) == 0 :
                companyName = div.xpath('div[1]/div[2]/div[1]/div[1]/h2/a/text()').extract()
            mainProduct = div.xpath('.//div[@class="value ellipsis ph"]//text()').extract()
            if 'China' in mainProduct:
                mainProduct = ''
            mainMarket = div.xpath('.//span[contains(@data-mark,"TR")]/text()').extract()

            tradingVolume = div.xpath('.//ul[@class="record util-clearfix"]/li/div/b/text()').extract()
            if len(tradingVolume) == 0 :
                tradingVolume = '0'
            else:
                tradingVolume = str(tradingVolume)[2:-2]
            transactionAmount = div.xpath('.//ul[@class="record util-clearfix"]/li/div[2]/text()').extract()
            transactionAmount = str(transactionAmount).replace(' ', '').replace('\\n', '').replace('\'', '').replace(
                '+', '').replace('$', '').replace(',', '').replace('[', '').replace(']', '')
            if len(transactionAmount) == 0:
                transactionAmount = '0'
            try:
                companyName = companyName[0]
            except:
                companyName = ''
            mainProduct = str(mainProduct)[2:-2]
            mainMarket = str(mainMarket)[2:-2]

            companyNames.append(companyName)
            areas.append(companyName.split(' ')[0])
            mainProducts.append(mainProduct)
            mainMarkets.append(mainMarket)
            tradingVolumes.append(tradingVolume)
            transactionAmounts.append(transactionAmount)
        # 赋值数据
        for i in range(0,len(companyNames)):
            item = aLiSupplyFileMain_Item()
            item['companyName'] = companyNames[i]
            item['number'] = numbers
            item['area'] = areas[i]
            item['mainProducts'] = mainProducts[i]
            item['mainMarket'] = mainMarkets[i]
            item['tradingVolume'] = tradingVolumes[i]
            item['transactionAmount'] = transactionAmounts[i]
            items.append(item)
        print(response.url)
        surl = response.url
        count = surl.rfind('=')
        reurl = surl[count+1:]
        self.next.remove(reurl)
        if self.next:
            r = scrapy.Request(url=self.head+self.next[0],callback=self.parse)
            items.append(r)
        elif len(self.next) == 0:
            print('更新Spider完成 , 更新数据名称 : https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.9e19459b8XUEfx&viewType=L&n=50&indexArea=company_en&keyword=children_clothes&page=1&f1=y')
        return items