# -*- coding: utf-8 -*-
import json

import scrapy

from children_1688.items import aliindex_7_hot_Item


class aliindex_30_hotSpider(scrapy.Spider):
    name = 'aliindex_30_hot'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/offer/rank.json?cat=311&dim=trade&period=month&time=1570687152200']
    names = ['所有', '儿童防晒衣/皮肤衣','儿童内衣内裤','儿童袜', '连身衣、爬服', '亲子装', '童T恤', '童背心/吊带', '童表演服/舞', '童衬衫', '童打底裤', '童打底衫', '童家居服', '童裤', '童礼服', '童马甲', '童毛衣', '童棉衣', '童牛仔服', '童披风/斗蓬', '童皮草/皮毛', '童皮衣', '童旗袍/唐装', '童裙', '童套装', '童外套/夹克', '童卫衣', '童羽绒服/羽', '童针织衫', '童装加工定制', '童装杂款包', '校服/校服定', '婴儿礼盒']
    urls = ['https://index.1688.com/alizs/offer/rank.json?cat=311&dim=trade&period=month&time=1570687152200',
            'https://index.1688.com/alizs/offer/rank.json?cat=127424004&dim=trade&period=month&time=1570687273341',
            'https://index.1688.com/alizs/offer/rank.json?cat=127496001&dim=trade&period=month&time=1570687350113',
            'https://index.1688.com/alizs/offer/rank.json?cat=1043351&dim=trade&period=month&time=1570687384466',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037003&dim=trade&period=month&time=1570687417466',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037039&dim=trade&period=month&time=1570687450589',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037012&dim=trade&period=month&time=1570687487483',
            'https://index.1688.com/alizs/offer/rank.json?cat=1048174&dim=trade&period=month&time=1570687515999',
            'https://index.1688.com/alizs/offer/rank.json?cat=122086001&dim=trade&period=month&time=1570687545769',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037011&dim=trade&period=month&time=1570687579288',
            'https://index.1688.com/alizs/offer/rank.json?cat=127430003&dim=trade&period=month&time=1570687615230',
            'https://index.1688.com/alizs/offer/rank.json?cat=127430004&dim=trade&period=month&time=1570687642063',
            'https://index.1688.com/alizs/offer/rank.json?cat=1042754&dim=trade&period=month&time=1570687668045',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037004&dim=trade&period=month&time=1570687708386',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037649&dim=trade&period=month&time=1570687734819',
            'https://index.1688.com/alizs/offer/rank.json?cat=1042841&dim=trade&period=month&time=1570687764001',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037010&dim=trade&period=month&time=1570687794139',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037006&dim=trade&period=month&time=1570687820768',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037007&dim=trade&period=month&time=1570687852408',
            'https://index.1688.com/alizs/offer/rank.json?cat=122704004&dim=trade&period=month&time=1570687880661',
            'https://index.1688.com/alizs/offer/rank.json?cat=124188006&dim=trade&period=month&time=1570687908307',
            'https://index.1688.com/alizs/offer/rank.json?cat=124196006&dim=trade&period=month&time=1570687933559',
            'https://index.1688.com/alizs/offer/rank.json?cat=122086002&dim=trade&period=month&time=1570687962279',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037005&dim=trade&period=month&time=1570687992389',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037192&dim=trade&period=month&time=1570688019080',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037648&dim=trade&period=month&time=1570688042890',
            'https://index.1688.com/alizs/offer/rank.json?cat=1042840&dim=trade&period=month&time=1570688064879',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037008&dim=trade&period=month&time=1570688087840',
            'https://index.1688.com/alizs/offer/rank.json?cat=1037009&dim=trade&period=month&time=1570688112041',
            'https://index.1688.com/alizs/offer/rank.json?cat=126440003&dim=trade&period=month&time=1570688136584',
            'https://index.1688.com/alizs/offer/rank.json?cat=127164001&dim=trade&period=month&time=1570688165947',
            'https://index.1688.com/alizs/offer/rank.json?cat=122088001&dim=trade&period=month&time=1570688188234',
            'https://index.1688.com/alizs/offer/rank.json?cat=122698004&dim=trade&period=month&time=1570688213424']

    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aliIndex_30_hot_Pipelines': 300}
    }

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
