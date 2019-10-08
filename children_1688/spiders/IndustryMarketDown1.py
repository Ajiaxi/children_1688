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
    - 用法: 控制台输入 scrapy crawl IndustryMarketDown1 --nolog 输入文件看pipelines中的类IndustryMarketDown 可改写文件路径
    - 参数解析：
            - category1： 种类一 就是童装的意思
            - category2： 种类2 也就是童装下的二级目录
            - industry_Type： 热门行业/潜力行业
            - purchaseIndex1688s： 1688采购指数
            - supplyIndexs： 1688供应指数
            - crawl_Time： 爬取数据日期
            - divs： li标签下的所有div 接下来遍历该div,获取所需数据
    - bug残留：  9.30下午 mark,待添加遍历所有网页获取数据      
                10.1 遍历网页后获得的数据无序 无解 只能一个网页写一个spider  
                解决了遍历所有网页问题 但还有另外的问题，和attribute一样的问题，不知道热门行业和潜力行业何时插入好
                '童装,儿童防晒衣/皮肤衣,潜力行业,童羽绒服/,"1,719","2,453",2019-10-05 17:54:17'
                10.6 写两个spider 爬取潜力行业和热门行业 热门行业的数据追加到潜力行业中去即可
'''

class IndustrymarketdownSpider(scrapy.Spider):
    name = 'IndustryMarketDown1'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127424004']
    urls2 = ['https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127424004',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127496001',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1043351',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037003',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037039',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037012',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1048174',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122086001',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037011',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127430003',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127430004',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042754',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037004',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037649',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042841',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037010',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037006',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037007',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122704004',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,124188006',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,124196006',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122086002',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037005',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037192',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037648',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042840',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037008',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037009',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,126440003',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127164001',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122088001',
             'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122698004']
    custom_settings = {
        'ITEM_PIPELINES' : {'children_1688.pipelines.IndustryMarketDown1': 300,}
    }

    def parse(self, response):
        category1 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[1]/p/a/text()').extract()
        category2 = response.xpath('//*[@id="aliindex-masthead"]/div/div[3]/div[2]/p/a/text()').extract()
        industry_Type = ['潜力行业']
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
        category1 = str(category1)[2:-2]
        category2 = str(category2)[2:-2]
        industry_Name1 = str(industry_Name1)[2:-2]
        purchaseIndex16881 = str(purchaseIndex16881)[2:-2]
        supplyIndex1 = str(supplyIndex1)[2:-2]
        list_industry_Name.append(industry_Name1)
        list_purchaseIndex1688.append(purchaseIndex16881)
        list_supplyIndex.append(supplyIndex1)
        items = []

        for div in divs:
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
            item = IndustrymarketdownItem()
            item['category1'] = category1
            item['category2'] = category2
            item['industry_Type'] = industry_Type[0]
            item['crawl_Time'] = crawl_Time
            item['industry_Name'] = list_industry_Name[i]
            item['purchaseIndex1688'] = list_purchaseIndex1688[i]
            item['supplyIndex'] = list_supplyIndex[i]
            items.append(item)
            # print(item)
        print(str(response.url)+'爬取完成')
        self.urls2.remove(response.url)

        if self.urls2:
            print('正在爬取：'+str(self.urls2[0]))
            r = scrapy.Request(url=self.urls2[0],callback=self.parse)
            items.append(r)
        return items