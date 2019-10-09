# -*- coding: utf-8 -*-
import json
import time
import scrapy
from children_1688.items import aliIndex_7_3_Item

'''
    陈航
    爬取童装 所有 阿里排行 搜索排行榜 最近7天数据 , 共4个排行榜 每个排行榜50条数据
    用法： scrapy crawl aliindex_7_3
    此spider为童装转化率榜
    
'''

class AliindexSpider(scrapy.Spider):
    name = 'aliindex_7_3'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=new&period=week']

    urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=new&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=word&period=week']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aliIndex_7_3_Pipelines': 300, },
    }

    def parse(self, response):
        # print(response.text)
        dics = json.loads(response.text)['content']
        keywords = []
        rates = []
        totals = []
        urls = []
        items = []
        for dic in dics:
            keywords.append(dic.get('keyword'))
            rates.append(dic.get('rate'))
            totals.append(dic.get('total'))
            urls.append(dic.get('url'))
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        for i in range(0,len(keywords)):
            item = aliIndex_7_3_Item()
            item['category1'] = '童装'
            item['category2'] = '所有'
            item['attribute_Type'] = '童装转化率榜'
            item['attribute_Name'] = keywords[i]
            item['rate'] = rates[i]
            item['total'] = totals[i]
            item['url'] = urls[i]
            item['crawl_Time'] = crawl_Time
            # print(item)
            items.append(item)
        return items