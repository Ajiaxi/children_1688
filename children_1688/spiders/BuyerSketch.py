# -*- coding: utf-8 -*-
import scrapy

'''
    陈航
    用途：爬取采购商素描栏目 童装所有
'''

class BuyersketchSpider(scrapy.Spider):
    name = 'BuyerSketch'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/purchaser.htm?userType=purchaser&cat=311']

    def parse(self, response):
        pass
