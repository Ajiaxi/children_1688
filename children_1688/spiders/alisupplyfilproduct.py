# -*- coding: utf-8 -*-
import time

import scrapy

from children_1688.items import aLiSupplyFileProduct_Item
from children_1688.logger import Logger


class AlisupplyfilproductSpider(scrapy.Spider):
    name = 'alisupplyfilproduct'
    allowed_domains = ['alibaba.com']
    start_urls = [
        'https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.1f86459bWExbQ1&n=38&f1=y&indexArea=company_en&viewType=L&keyword=children_clothes&page=1']
    head = 'https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.1f86459bWExbQ1&n=38&f1=y&indexArea=company_en&viewType=L&keyword=children_clothes&page='
    next = []
    for i in range(1, 58):
        next.append(str(i))
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aLiSupplyFileProduct_pipelines': 300, },
    }

    def parse(self, response):
        divs = response.xpath('.//div[@class="item-main"]')
        companyNames = []
        numbers = 1
        mainProducts = []
        items = []
        mainPro = []
        # 获取数据
        for div in divs:
            companyName = div.xpath('div[1]/div[2]/div[1]/div[2]/h2/a/text()').extract()
            crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            if len(companyName) == 0:
                companyName = div.xpath('div[1]/div[2]/div[1]/div[1]/h2/a/text()').extract()
            mainProduct = div.xpath('.//div[@class="value ellipsis ph"]/text()').extract()
            if len(mainProduct) > 0:
                mainProduct = str(mainProduct)[1:-1]
                mainProduct = mainProduct.replace('\'','').replace(' ','')
                mainProduct = mainProduct.split(',')
            else:
                mainProduct = ''
            for i in range(0,len(mainProduct)):
                if mainProduct[i] != '':
                    mainPro.append(mainProduct[i])
            if 'China' in mainPro:
                mainPro = ''
            try:
                companyName = companyName[0]
            except:
                companyName = ''
            if len(mainPro) > 0 :
                for i in range(0,len(mainPro)):
                    companyNames.append(companyName)
                    mainProducts.append(mainPro[i])
            else:
                companyNames.append(companyName)
                mainProducts.append(' ')
        # 赋值数据
        for i in range(0, len(companyNames)):
            item = aLiSupplyFileProduct_Item()
            item['companyName'] = companyNames[i]
            item['product'] = mainProducts[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        surl = response.url
        count = surl.rfind('=')
        reurl = surl[count + 1:]
        self.next.remove(reurl)
        if self.next:
            r = scrapy.Request(url=self.head + self.next[0], callback=self.parse)
            items.append(r)
        elif len(self.next) == 0:
            print(
                '更新Spider完成 , 更新数据名称 : alisupplyfilproduct')
            Logger('all.log', level='debug').logger.info('更新Spider完成 , 更新数据名称 : alisupplyfilproduct')
        return items