# -*- coding: utf-8 -*-
import json
import time
import scrapy
from children_1688.items import AttributeSegmentationPriceItem
'''
    爬取属性细分价格带分布
'''

class PriceSpider(scrapy.Spider):
    name = 'AttributeSegmentationPrice'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,127424004']
    next = ['127424004', '127496001', '1043351', '1037003', '1037039',
            '1037012', '1048174', '122086001', '1037011', '127430003',
            '127430004', '1042754', '1037004', '1037649', '1042841',
            '1037010', '1037006', '1037007', '122704004', '124188006',
            '124196006', '122086002', '1037005', '1037192', '1037648',
            '1042840', '1037008', '1037009', '126440003', '127164001',
            '122088001', '122698004']
    url = 'https://index.1688.com/alizs/attr/price.json?userType=purchaser&cat=311,'
    category2 = ['儿童防晒衣/皮肤衣', '儿童内衣内裤', '儿童袜', '连身衣、爬服', '亲子装', '童T恤', '童背心/吊带', '童表演服/舞', '童衬衫', '童打底裤', '童打底衫',
                 '童家居服', '童裤', '童礼服', '童马甲', '童毛衣', '童棉衣', '童牛仔服', '童披风/斗蓬', '童皮草/皮毛', '童皮衣', '童旗袍/唐装', '童裙', '童套装',
                 '童外套/夹克', '童卫衣', '童羽绒服/羽', '童针织衫', '童装加工定制', '童装杂款包', '校服/校服定', '婴儿礼盒']
    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.AttributeSegmentationPricePipelines': 300,},
    }

    # 处理数据的方法　返回items
    def datadeal(self,data,items):
        browserdataLists = data['content']['browser']
        tradedataLists = data['content']['trade']
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        index_Types = []
        percentages = []
        index_Types1 = []
        percentages1 = []
        # 浏览商品价格分布
        for dataList in browserdataLists:
            index_Types.append(dataList['name'])
            percentages.append(dataList['value'])
        category = self.category2[0]
        # 交易商品价格分布
        for dataList in tradedataLists:
            index_Types1.append(dataList['name'])
            percentages1.append(dataList['value'])
        # 循环赋值进item中
        for i in range(0, len(index_Types)):
            item = AttributeSegmentationPriceItem()
            item['category1'] = '童装'
            item['category2'] = category
            item['attribute_Type'] = '价格带分布'
            item['attribute_Name'] = '1688浏览商品价格分布'
            item['index_Type'] = index_Types[i]
            item['percentage'] = percentages[i]
            item['attribute_Name1'] = '1688交易商品价格分布'
            item['index_Type1'] = index_Types1[i]
            item['percentage1'] = percentages1[i]
            item['crawl_Time'] = crawl_Time
            items.append(item)
        return items,category

    # 处理第一个页面的parse
    def parse(self, response):
        print('正在爬取Spider..... , 爬取名称 : 1688网站属性细分价格带分布')
        data = json.loads(response.text)
        items = []
        items , category = self.datadeal(data,items)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count + 1:]
        self.next.remove(resurl)
        self.category2.remove(category)
        if self.next:
            r = scrapy.Request(url=self.url+self.next[0],callback=self.next_parse)
            items.append(r)
        return items

    # 处理后续页面的parse
    def next_parse(self,response):
        data = json.loads(response.text)
        items = []
        items, category = self.datadeal(data, items)
        surl = str(response.url)
        count = surl.find(',')
        resurl = surl[count+1:]
        self.next.remove(resurl)
        self.category2.remove(category)
        if self.next:
            r = scrapy.Request(url=self.url+self.next[0],callback=self.next_parse)
            items.append(r)
        elif len(self.next) == 0:
            print('爬取Spider完成..... , 爬取名称 : 1688网站属性细分价格带分布')
        return items








