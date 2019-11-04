# -*- coding: utf-8 -*-
import json
import time

import scrapy

from children_1688.items import Cmindexchild_Item


class CmindexchildSpider(scrapy.Spider):
    name = 'cmindexchild'
    allowed_domains = ['zlzgtzzs.com']
    start_urls = ['http://www.zlzgtzzs.com/webapi/index/project/88/data?structCode=root']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.Cmindexchild_pipelines': 300, },
    }
    def parse(self, response):
        data = json.loads(response.text)
        index = []
        date = []
        dealdate = []
        dealIndex = []
        for d in data['data']:
            index.append(d.get('indexValue'))
            date.append(d.get('publishTime'))
        for i in index:
            dealIndex.append(round(i,2))
        count = date.index('2018-03-30')
        dealIndex = dealIndex[0:count + 1]
        date = date[0:count+1]
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        for d in date:
            dYear = d[:4]
            dMonth = d[5:7]
            if dYear == '2020':
                if dMonth == '12': dealdate.append('2020Q4')
                elif dMonth == '09': dealdate.append('2020Q3')
                elif dMonth == '06': dealdate.append('2020Q2')
                elif dMonth == '03': dealdate.append('2020Q1')
            elif dYear == '2019':
                if dMonth == '12': dealdate.append('2019Q4')
                elif dMonth == '09': dealdate.append('2019Q3')
                elif dMonth == '06': dealdate.append('2019Q2')
                elif dMonth == '03': dealdate.append('2019Q1')
            elif dYear == '2018':
                if dMonth == '12': dealdate.append('2018Q4')
                elif dMonth == '09': dealdate.append('2018Q3')
                elif dMonth == '06': dealdate.append('2018Q2')
                elif dMonth == '03': dealdate.append('2018Q1')
        for i in range(0,len(dealdate)):
            item = Cmindexchild_Item()
            item['number'] = str(i+1)
            item['date'] = dealdate[i]
            item['index'] = str(dealIndex[i])
            item['crawl_Time'] = crawl_Time
            yield item
        print('更新Spider完成 , 更新数据名称 : cmindexchild')


