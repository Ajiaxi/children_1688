# -*- coding: utf-8 -*-
import json
import time
import scrapy
from children_1688.items import aliIndex_7_1_Item

'''
    陈航 这与scrapy项目无关, 是我用于爬取贴吧文章的code
    
    http://www.369hi.com/p/10306/pu/1
    
    http://www.369hi.com/p/10306/pu/1551
'''

class article_first_love(scrapy.Spider):
    name = 'love'
    allowed_domains = ['1688.com']
    start_urls = ['http://www.369hi.com/p/10306/pu/1']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aliIndex_7_1_Pipelines': 300, },
    }

    def parse(self, response):
        divs = response.xpath('.//div[@class="content round mb-2"]').extract()
        for div in divs:
            print(div)