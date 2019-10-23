# -*- coding: utf-8 -*-
import datetime
import json
import time

import scrapy

from children_1688.items import Cmindexpricefabric_Item


class CmindexpricefabricSpider(scrapy.Spider):
    name = 'cmindexPriceFabric'
    allowed_domains = ['kqindex.cn']
    start_urls = ['http://www.kqindex.cn/flzs/table_data?category=3&start=&end=&indexType=1_1&pageindex=1&_=1571796974741']
    head = 'http://www.kqindex.cn/flzs/table_data?category=3&start=&end=&indexType=1_1&pageindex='
    end = '&_=1571796974741'
    next = []
    for i in range(1,51):
        next.append(str(i))
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.Cmindexpricefabric_pipelines': 300, },
    }

    def parse(self, response):
        jsonData = json.loads(response.text)
        datas = jsonData['result']
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        date = []
        index = []
        index_hb = []
        items = []
        for data in datas:
            date.append(data.get('round'))
            index.append(data.get('index'))
            index_hb.append(data.get('index_hb'))
        for i in range(0,len(date)):
            item = Cmindexpricefabric_Item()
            item['date'] = date[i]
            item['index'] = index[i]
            item['index_hb'] = index_hb[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        count = str(response.url).rfind('&')
        reurl = str(response.url)[count-2:count]
        if '=' in reurl:
            reurl = str(response.url)[count-1:count]
        self.next.remove(reurl)
        if len(reurl) > 0:
            try:
                r = scrapy.Request(url=self.head + self.next[0] + self.end,callback=self.parse)
                items.append(r)
            except:
                print('CmindexpricefabricSpider爬取完成')
        return items
