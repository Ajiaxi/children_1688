# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import FormRequest

from children_1688.items import priceItem

'''
    用法： scrapy crawl price
    bug残留： 10.5 晚 只能获取一次，并且也是相同的price.json get 
            10.6  分类2栏目赋值不知如何做
    
'''

class PriceSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,127424004']
    urls = ['https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,127424004',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,127496001',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1043351',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037003',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037039',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037012',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1048174',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,122086001',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037011',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,127430003',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,127430004',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1042754',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037004',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037649',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1042841',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037010',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037006',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037007',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,122704004',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,124188006',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,124196006',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,122086002',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037005',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037192',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037648',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1042840',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037008',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,1037009',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,126440003',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,127164001',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,122088001',
            'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,122698004']
    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.PricePipelines': 300,},
    }

    def parse(self, response):
        category2 = ['儿童防晒衣/皮肤衣', '儿童内衣内裤', '儿童袜', '连身衣、爬服', '亲子装', '童T恤', '童背心/吊带', '童表演服/舞', '童衬衫', '童打底裤', '童打底衫', '童家居服', '童裤', '童礼服', '童马甲', '童毛衣', '童棉衣', '童牛仔服', '童披风/斗蓬', '童皮草/皮毛', '童皮衣', '童旗袍/唐装', '童裙', '童套装', '童外套/夹克', '童卫衣', '童羽绒服/羽', '童针织衫', '童装加工定制', '童装杂款包', '校服/校服定', '婴儿礼盒']
        data = json.loads(response.text)
        dataLists = data['content']['browser']
        index_Types = []
        percentages = []
        items = []

        for dataList in dataLists:
            index_Types.append(dataList['name'])
            percentages.append(dataList['value'])

        for i in range(0,len(index_Types)):
            item = priceItem()
            item['category1'] = '童装'
            item['category2'] = category2[0]
            item['attribute_Type'] = '价格带分布'
            item['attribute_Name'] = '1688浏览商品分布'
            item['index_Type'] =  index_Types[i]
            item['percentage'] =  percentages[i]
            # yield item
            items.append(item)

        print('爬取完成：'+ response.url)
        self.urls.remove(response.url)
        if self.urls:
            print('正在爬取：'+self.urls[0])
            r = scrapy.Request(url=self.urls[0],callback=self.parse)
            items.append(r)
        return items






