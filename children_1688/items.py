# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Children1688Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
     purchaseIndex1688 1688采购指数
     purchaseIndexTb 淘宝采购指数
     supplyIndex   1688供应指数
      category1	 category2　　　　time	     purchaseIndex1688     purchaseIndexTb	     supplyIndex       　　　crawl_Time
		童装	　      所有　　　　2018/9.27  　　 1688采购指数/淘宝采购指数/1688供应指数　　32191　　　2019/9.30
    '''
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    showtime = scrapy.Field()
    purchaseIndex1688 = scrapy.Field()
    purchaseIndexTb = scrapy.Field()
    supplyIndex = scrapy.Field()
    crawl_Time = scrapy.Field()


class SecondIndexItem(scrapy.Item):
    '''
    - category1    category2    showtime    1688采购指数    1688供应指数       爬取时间
        童装    　防晒衣　　　　2018 / 9.27    数据              数据         2019 / 9.30                   32    个csv
     '''
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    showtime = scrapy.Field()
    purchaseIndex1688 = scrapy.Field()
    supplyIndex = scrapy.Field()
    crawl_Time = scrapy.Field()

class IndustrymarketdownItem(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    industry_Type = scrapy.Field()
    industry_Name = scrapy.Field()
    purchaseIndex1688 = scrapy.Field()
    supplyIndex = scrapy.Field()
    crawl_Time = scrapy.Field()


class AttributesegmentationItem(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    industry_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    attribute_Type = scrapy.Field()
    purchaseIndex = scrapy.Field()
    supplyIndex = scrapy.Field()
    crawl_Time = scrapy.Field()

class priceItem(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    attribute_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    index_Type = scrapy.Field()
    percentage = scrapy.Field()