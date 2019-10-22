# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Children1688Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    category1 = scrapy.Field()
    category2 = scrapy.Field()
    showtime = scrapy.Field()
    purchaseIndex1688 = scrapy.Field()
    purchaseIndexTb = scrapy.Field()
    supplyIndex = scrapy.Field()
    crawl_Time = scrapy.Field()

class SecondIndexItem(scrapy.Item):
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
    demand_Forecast = scrapy.Field()
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

class AttributeSegmentationMiddleItem(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    industry_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    purchaseIndex = scrapy.Field()
    supplyIndex = scrapy.Field()
    crawl_Time = scrapy.Field()

class AttributeSegmentationPriceItem(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    attribute_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    index_Type = scrapy.Field()
    percentage = scrapy.Field()
    attribute_Name1 = scrapy.Field()
    index_Type1 = scrapy.Field()
    percentage1 = scrapy.Field()
    crawl_Time = scrapy.Field()

class BuyerSketchItem(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    attribute_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    percentage = scrapy.Field()
    attribute_Name1 = scrapy.Field()
    percentage1 = scrapy.Field()
    crawl_Time = scrapy.Field()

class aliIndex_7_1_Item(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    attribute_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    search_Trend = scrapy.Field()
    index  = scrapy.Field()
    url = scrapy.Field()
    crawl_Time = scrapy.Field()

class aliIndex_7_2_Item(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    attribute_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    index = scrapy.Field()
    total  = scrapy.Field()
    url = scrapy.Field()
    crawl_Time = scrapy.Field()

class aliIndex_7_3_Item(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    attribute_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    rate = scrapy.Field()
    total  = scrapy.Field()
    url = scrapy.Field()
    crawl_Time = scrapy.Field()

class aliIndex_7_4_Item(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    attribute_Type = scrapy.Field()
    attribute_Name = scrapy.Field()
    index = scrapy.Field()
    total  = scrapy.Field()
    url = scrapy.Field()
    crawl_Time = scrapy.Field()

class aliindex_7_hot_Item(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    trade = scrapy.Field()

class aLiSupplyFileMain_Item(scrapy.Item):
    companyName = scrapy.Field()
    number = scrapy.Field()
    area = scrapy.Field()
    mainProducts = scrapy.Field()
    mainMarket = scrapy.Field()
    tradingVolume = scrapy.Field()
    transactionAmount = scrapy.Field()

class aLiSupplyFileMarket_Item(scrapy.Item):
    companyName = scrapy.Field()
    number = scrapy.Field()
    area = scrapy.Field()
    mainMarket = scrapy.Field()

class aLiSupplyFileProduct_Item(scrapy.Item):
    companyName = scrapy.Field()
    number = scrapy.Field()
    product = scrapy.Field()