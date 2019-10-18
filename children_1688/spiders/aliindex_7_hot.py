# -*- coding: utf-8 -*-
import json

import scrapy
from children_1688.items import aliindex_7_hot_Item

class aliindex_7_hotSpider(scrapy.Spider):
    name = 'aliindex_7_hot'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/offer/rank.json?cat=311&dim=trade&period=week&time=1570686769180']
    next = ['311', '127424004', '127496001', '1043351', '1037003', '1037039',
            '1037012', '1048174', '122086001', '1037011', '127430003',
            '127430004', '1042754', '1037004', '1037649', '1042841',
            '1037010', '1037006', '1037007', '122704004', '124188006',
            '124196006', '122086002', '1037005', '1037192', '1037648',
            '1042840', '1037008', '1037009', '126440003', '127164001',
            '122088001', '122698004']
    head = 'https://index.1688.com/alizs/offer/rank.json?cat='
    end = '&dim=trade&period=week&time=1570686631309'

    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aliIndex_7_hot_Pipelines': 300}
    }
    names = ['所有', '儿童防晒衣/皮肤衣', '儿童内衣内裤', '儿童袜', '连身衣、爬服', '亲子装', '童T恤', '童背心/吊带', '童表演服/舞', '童衬衫', '童打底裤', '童打底衫',
             '童家居服', '童裤', '童礼服', '童马甲', '童毛衣', '童棉衣', '童牛仔服', '童披风/斗蓬', '童皮草/皮毛', '童皮衣', '童旗袍/唐装', '童裙', '童套装',
             '童外套/夹克', '童卫衣', '童羽绒服/羽', '童针织衫', '童装加工定制', '童装杂款包', '校服/校服定', '婴儿礼盒']

    # 把名字作为参数传递
    def parse(self, response, name=names):
        node_list = json.loads(response.text)['content']['hot']
        for node in node_list:
            item = aliindex_7_hot_Item()
            item["name"] = name[0]
            item["type"] = '热销榜'
            item["title"] = node.get('title')
            item["price"] = node.get('price')
            item["trade"] = node.get('trade')
            yield item
        surl = str(response.url)
        start = surl.find('=')
        end = surl.find('&')
        resurl = surl[start + 1: end]
        if resurl == '311':
            print('正在更新Spider , 更新数据名称 : 1688网站阿里排行产品排行榜')
        self.next.remove(resurl)
        if self.next:
            r = scrapy.Request(url=self.head+self.next[0]+self.end, callback=self.parse)
            self.names.remove(self.names[0])
            yield r
        elif len(self.next):
            print('更新Spider完成 , 更新数据名称 : 1688网站阿里排行产品排行榜')














