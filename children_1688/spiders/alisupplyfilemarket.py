# -*- coding: utf-8 -*-
import time

import scrapy

from children_1688.items import aLiSupplyFileMarket_Item
from children_1688.logger import Logger


class AlisupplyfilemarketSpider(scrapy.Spider):
    name = 'alisupplyfilemarket'
    allowed_domains = ['alibaba.com']
    start_urls = [
        'https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.1f86459bWExbQ1&n=38&f1=y&indexArea=company_en&viewType=L&keyword=children_clothes&page=1']
    head = 'https://www.alibaba.com/trade/search?spm=a2700.supplier-normal.16.4.1f86459bWExbQ1&n=38&f1=y&indexArea=company_en&viewType=L&keyword=children_clothes&page='
    next = []
    for i in range(1, 58):
        next.append(str(i))
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aLiSupplyFileMarket_pipelines': 300, },
    }

    def parse(self, response):
        divs = response.xpath('.//div[@class="item-main"]')
        companyNames = []
        numbers = 1
        areas = []
        mainMarkets = []
        items = []
        # 获取数据
        for div in divs:
            companyName = div.xpath('div[1]/div[2]/div[1]/div[2]/h2/a/text()').extract()
            crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            if len(companyName) == 0:
                companyName = div.xpath('div[1]/div[2]/div[1]/div[1]/h2/a/text()').extract()
            midd = div.xpath('.//span[contains(@data-mark,"TR")]/text()').extract()
            if len(midd) == 0:
                mainMarkets.append(0)
            middarea = []
            middcount = []
            for i in range(0,len(midd)):
                count = midd[i].rfind(' ')
                middarea.append(str(midd[i])[:count])
                middcou = str(midd[i])[count+1:]
                middcou = middcou.strip('%')
                middcou = float(middcou)
                middcount.append(int(middcou)/100)
            try:
                companyName = companyName[0]
            except:
                companyName = ''
            if len(midd) >= 1 :
                for i in range(0,len(midd)):
                    companyNames.append(companyName)
                    areas.append(middarea[i])
            else:
                companyNames.append(companyName)
                areas.append(' ')
            for m in middcount:
                mainMarkets.append(m)

        # 赋值数据
        for i in range(0, len(companyNames)):
            item = aLiSupplyFileMarket_Item()
            item['companyName'] = companyNames[i]
            item['area'] = areas[i]
            item['mainMarket'] = str(mainMarkets[i])
            item['crawl_Time'] = crawl_Time
            items.append(item)
        surl = response.url
        count = surl.rfind('=')
        reurl = surl[count + 1:]
        self.next.remove(reurl)
        if self.next:
            r = scrapy.Request(url=self.head + self.next[0], callback=self.parse)
            items.append(r)
        return items