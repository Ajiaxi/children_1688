# -*- coding: utf-8 -*-
import json
import time
import scrapy
from children_1688.items import aliIndex_7_4_Item

'''
    陈航
    爬取童装 所有 阿里排行 搜索排行榜 最近7天数据 , 共4个排行榜 每个排行榜50条数据
    用法： scrapy crawl aliindex_7_4
    此spider为童装新词榜
    
'''

class AliindexSpider(scrapy.Spider):
    name = 'aliindex_7_4'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=word&period=week']

    urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=word&period=week']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aliIndex_7_4_Pipelines': 300, },
    }

    def parse(self, response):
        # print(response.text)
        dics = json.loads(response.text)['content']
        keywords = []
        indexs = []
        totals = []
        urls = []
        items = []
        for dic in dics:
            keywords.append(dic.get('keyword'))
            indexs.append(dic.get('index'))
            totals.append(dic.get('total'))
            urls.append(dic.get('url'))
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        for i in range(0,len(keywords)):
            item = aliIndex_7_4_Item()
            item['category1'] = '童装'
            item['category2'] = '所有'
            item['attribute_Type'] = '童装新词榜'
            item['attribute_Name'] = keywords[i]
            item['index'] = indexs[i]
            item['total'] = totals[i]
            item['url'] = urls[i]
            item['crawl_Time'] = crawl_Time
            # print(item)
            items.append(item)
        return items