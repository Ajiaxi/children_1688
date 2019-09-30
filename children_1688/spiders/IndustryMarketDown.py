# -*- coding: utf-8 -*-
import time
import scrapy
from children_1688.items import IndustrymarketdownItem

'''
    - 陈航
    - 爬取行业大盘下面 最近30天儿童防晒衣/皮肤衣相关行业
    - 思路: 网页数据分为两部分,例如儿童防晒衣这个网页,上面为儿童防晒衣,下面为5行,
            先获取上面行也就岁儿童防晒衣的数据,接着获取下面五行的数据,相同数据不用理会,
            不同数据需要拼接在一起,然后遍历赋值给item即可
    - 用法: 控制台输入 scrapy crawl IndustryMarketDown 输入文件看pipelines中的类IndustryMarketDown 可改写文件路径
    - 参数解析：
            - category1： 种类一 就是童装的意思
            - category2： 种类2 也就是童装下的二级目录
            - industry_Type： 热门行业/潜力行业
            - purchaseIndex1688s： 1688采购指数
            - supplyIndexs： 1688供应指数
            - crawl_Time： 爬取数据日期
            - divs： li标签下的所有div 接下来遍历该div,获取所需数据
    - bug残留：  9.30下午 mark,待添加遍历所有网页获取数据        
'''

class IndustrymarketdownSpider(scrapy.Spider):
    name = 'IndustryMarketDown'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127424004']
    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.IndustryMarketDown': 300,}
    }

    def parse(self, response):
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract()
        category2 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[2]/p/a/text()').extract()
        industry_Type = response.xpath('//*[@id="mod-related"]/div[1]/ul/li[1]/text()').extract()
        industry_Name1 = response.xpath('//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/p[1]/@title').extract()
        purchaseIndex16881 = response.xpath(
            '//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/div[2]/p/text()').extract()
        supplyIndex1 = response.xpath('//*[@id="mod-related"]/div[2]/div[1]/div[1]/div[2]/div[3]/p/text()').extract()
        crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        divs = response.xpath('//*[@id="mod-related"]/div[2]/div[1]/div[1]/ul/li')
        # 拼接数据
        list_industry_Name = []
        list_purchaseIndex1688 = []
        list_supplyIndex = []
        item = IndustrymarketdownItem()
        category1 = str(category1)[2:-2]
        category2 = str(category2)[2:-2]
        industry_Type = str(industry_Type)[2:-2]
        list_industry_Name.append(industry_Name1)
        list_purchaseIndex1688.append(purchaseIndex16881)
        list_supplyIndex.append(supplyIndex1)

        for i in range(0,len(divs)):
            div = divs[i]
            industry_Name2 = div.xpath('./div[1]/p[1]/text()').extract()
            purchaseIndex16882 = div.xpath('./div[1]/div[2]/p/text()').extract()
            supplyIndex2 = div.xpath('./div[1]/div[3]/p/text()').extract()
            industry_Name2 = str(industry_Name2)[2:-2]
            purchaseIndex16882 = str(purchaseIndex16882)[2:-2]
            supplyIndex2= str(supplyIndex2)[2:-2]
            list_industry_Name.append(industry_Name2)
            list_purchaseIndex1688.append(purchaseIndex16882)
            list_supplyIndex.append(supplyIndex2)

        for i in range(0,len(list_supplyIndex)):
            item['category1'] = category1
            item['category2'] = category2
            item['industry_Type'] = industry_Type
            item['crawl_Time'] = crawl_Time
            item['industry_Name'] = list_industry_Name[i]
            item['purchaseIndex1688'] = list_purchaseIndex1688[i]
            item['supplyIndex'] = list_supplyIndex[i]
            print(item)
            yield item

