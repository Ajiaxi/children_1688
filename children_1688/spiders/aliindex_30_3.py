# -*- coding: utf-8 -*-
import json
import time
import scrapy
from children_1688.items import aliIndex_7_3_Item

'''
    陈航
    爬取童装 所有 阿里排行 搜索排行榜 最近30天数据 , 共4个排行榜 每个排行榜50条数据
    用法： scrapy crawl aliindex_30_3  
    此spider为童装转化率榜
    
'''

class aliindex_30_3_spider(scrapy.Spider):
    name = 'aliindex_30_3'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=new&period=month']

    urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127424004&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127496001&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1043351&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037003&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037039&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037012&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1048174&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122086001&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037011&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127430003&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127430004&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1042754&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037004&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037649&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1042841&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037010&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037006&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037007&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122704004&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=124188006&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=124196006&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122086002&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037005&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037192&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037648&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1042840&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037008&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037009&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=126440003&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127164001&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122088001&rankType=new&period=month',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122698004&rankType=new&period=month']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aliIndex_30_3_Pipelines': 300, },
    }

    def parse(self, response):

        print('正在爬取,请稍等......')
        # print(response.text)
        data = json.loads(response.text)
        # print(len(data))
        keywords = []
        rates = []
        totals = []
        urls = []
        items = []
        if len(data) == 2:
            dics = data['content']
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
            print('爬取完成：' + str(response.url))
            self.urls.remove(response.url)
            if self.urls:
                r = scrapy.Request(url=self.urls[0], callback=self.parse)
                items.append(r)
            return items
        else:
            print('content无数据.....')
            self.urls.remove(response.url)
            if self.urls:
                r = scrapy.Request(url=self.urls[0], callback=self.parse)
                items.append(r)
            return items