# -*- coding: utf-8 -*-
import json

import scrapy
from children_1688.items import aliindex_7_hot_Item

class aliindex_7_hotSpider(scrapy.Spider):
    name = 'aliindex_7_hot'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/offer/rank.json?cat=311&dim=trade&period=week&time=1570686769180']

    urls = ['https://index.1688.com/alizs/offer/rank.json?cat=311&dim=trade&period=week&time=1570686769180',
            'https://index.1688.com/alizs/offer/rank.json?cat=127424004&dim=trade&period=week&time=1570686745789',
            'https://index.1688.com/alizs/offer/rank.json?cat=127496001&dim=trade&period=week&time=1570686730005',
            'https://index.1688.com/alizs/offer/rank.json?cat=1043351&dim=trade&period=week&time=1570686678756',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037003&dim=trade&period=week&time=1570671275367',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037039&dim=trade&period=week&time=1570671358423',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037012&dim=trade&period=week&time=1570679597471',
            'https://index.1688.com/alizs/offer/rank.json?cat=1048174&dim=trade&period=week&time=1570679650877',
            'https://index.1688.com/alizs/offer/rank.json?cat=122086001&dim=trade&period=week&time=1570679681823',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037011&dim=trade&period=week&time=1570679727030',
            'https://index.1688.com/alizs/offer/rank.json?cat=127430003&dim=trade&period=week&time=1570680158151',
            'https://index.1688.com/alizs/offer/rank.json?cat=127430004&dim=trade&period=week&time=1570680202856',
            'https://index.1688.com/alizs/offer/rank.json?cat=1042754&dim=trade&period=week&time=1570680232975',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037004&dim=trade&period=week&time=1570680257584',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037649&dim=trade&period=week&time=1570686185844',
            'https://index.1688.com/alizs/offer/rank.json?cat=1042841&dim=trade&period=week&time=1570686237269',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037010&dim=trade&period=week&time=1570686256633',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037006&dim=trade&period=week&time=1570686273753',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037007&dim=trade&period=week&time=1570686293475',
            'https://index.1688.com/alizs/offer/rank.json?cat=122704004&dim=trade&period=week&time=1570686336981',
            'https://index.1688.com/alizs/offer/rank.json?cat=124188006&dim=trade&period=week&time=1570686354666',
            'https://index.1688.com/alizs/offer/rank.json?cat=124196006&dim=trade&period=week&time=1570686377041',
            'https://index.1688.com/alizs/offer/rank.json?cat=122086002&dim=trade&period=week&time=1570686396920',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037005&dim=trade&period=week&time=1570686414832',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037192&dim=trade&period=week&time=1570686432156',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037648&dim=trade&period=week&time=1570686452605',
            'https://index.1688.com/alizs/offer/rank.json?cat=1042840&dim=trade&period=week&time=1570686470750',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037008&dim=trade&period=week&time=1570686492909',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037009&dim=trade&period=week&time=1570686509509',
            'https://index.1688.com/alizs/offer/rank.json?cat=126440003&dim=trade&period=week&time=1570686565736',
            'https://index.1688.com/alizs/offer/rank.json?cat=127164001&dim=trade&period=week&time=1570686595978',
            'https://index.1688.com/alizs/offer/rank.json?cat=122088001&dim=trade&period=week&time=1570686612190',
            'https://index.1688.com/alizs/offer/rank.json?cat=122698004&dim=trade&period=week&time=1570686631309']

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
        print('爬取完成：' + str(response.url))
        self.urls.remove(self.urls[0])
        if self.urls:
            r = scrapy.Request(url=self.urls[0], callback=self.parse)
            self.names.remove(self.names[0])
            yield r














