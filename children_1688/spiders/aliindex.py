# -*- coding: utf-8 -*-
import scrapy


class AliindexSpider(scrapy.Spider):
    name = 'aliindex'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=new&period=month']

    def parse(self, response):
        pass
