# -*- coding: utf-8 -*-
import json
import time

import scrapy

from children_1688.items import Cmindexsalegery_Item


class CmindexsalegreySpider(scrapy.Spider):
    name = 'cmindexSaleGrey'
    allowed_domains = ['kqindex.cn']
    start_urls = ['http://www.kqindex.cn/flzs/table_data?category=2&start=&end=&indexType=1_2&pageindex=1']
    head = 'http://www.kqindex.cn/flzs/table_data?category=2&start=&end=&indexType=1_2&pageindex='
    next = []
    for i in range(1, 5):
        next.append(str(i))
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.CmindexsaleGrey_pipelines': 300, },
    }

    def parse(self, response):
        jsonData = json.loads(response.text)
        datas = jsonData['result']
        date = []
        dealdate = []
        index = []
        index_hb = []
        bindex1 = []
        bindex2 = []
        items = []
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        for data in datas:
            date.append(data.get('round'))
            index.append(data.get('index'))
            index_hb.append(data.get('index_hb'))
            bindex1.append(data.get('bindex1'))
            bindex2.append(data.get('bindex2'))
        for d in date:
            dealdate.append(str(d).replace('年', '').replace('月', ''))
        for i in range(0, len(date)):
            item = Cmindexsalegery_Item()
            item['round'] = dealdate[i]
            item['index'] = index[i]
            item['index_hb'] = index_hb[i]
            item['bindex1'] = index_hb[i]
            item['bindex2'] = index_hb[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        reurl = str(response.url)[-2:]
        if '=' in reurl:
            reurl = str(response.url)[-1:]
        self.next.remove(reurl)
        if len(reurl) > 0:
            try:
                r = scrapy.Request(url=self.head + self.next[0], dont_filter=True, callback=self.parse)
                items.append(r)
            except:
                print('cmindexSaleGrey爬取完成')
        return items
