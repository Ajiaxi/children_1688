# -*- coding: utf-8 -*-
import json
import time

import scrapy

from children_1688.items import Cmindexpricefabric_Item


class CmindexpricegreySpider(scrapy.Spider):
    name = 'cmindexPriceGrey'
    allowed_domains = ['www.baidu.com']
    start_urls = [
        'http://www.kqindex.cn/flzs/table_data?category=2&start=&end=&indexType=1_1&pageindex=1&_=1571803141']
    head = 'http://www.kqindex.cn/flzs/table_data?category=2&start=&end=&indexType=1_1&pageindex='
    end = '&_='
    next = []
    t = time.time()
    t = str(t).split('.')[0]
    for i in range(1, 51):
        next.append(str(i))
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.cmindexPriceGrey_pipelines': 300, },
    }

    def parse(self, response):
        jsonData = json.loads(response.text)
        datas = jsonData['result']
        date = []
        index = []
        index_hb = []
        items = []
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        for data in datas:
            date.append(data.get('round'))
            index.append(data.get('index'))
            index_hb.append(data.get('index_hb'))
        for i in range(0, len(date)):
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
                u = self.head + self.next[0] + self.end
                r = scrapy.Request(url=u, dont_filter=True,callback=self.parse)
                items.append(r)
            except:
                print('CmindexpricegreySpider爬取完成')
        return items
