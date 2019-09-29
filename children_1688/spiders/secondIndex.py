# -*- coding: utf-8 -*-
import json

import scrapy

from children_1688.items import SecondIndexItem


class SecondindexSpider(scrapy.Spider):
    name = 'secondIndex'
    allowed_domains = ['index.1688.com']
    start_urls = ['https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127424004']
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127496001',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1043351',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037003',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037039',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037012',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1048174',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122086001',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037011',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127430003',
                  #
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127430004',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042754',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037004',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037649',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042841',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037010',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037006',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037007',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122704004',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,124188006',
                  #
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,124196006',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122086002',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037005',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037192',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037648',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1042840',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037008',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,1037009',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,126440003',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,127164001',
                  #
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122088001',
                  # 'https://index.1688.com/alizs/market.htm?userType=purchaser&cat=311,122698004',
                  # ]

    def parse(self, response):
        data = response.xpath('//*[@id="main-chart-val"]/@value').extract_first()
        datajson = json.loads(data)

        purchaseIndex1688s = datajson["purchaseIndex1688"]["index"]["history"]
        supplyIndexs = datajson['supplyIndex']["index"]["history"]

        for i in range(0, len(purchaseIndex1688s)):
            pIndex1688 = purchaseIndex1688s[i]
            supplyIndex = supplyIndexs[i]
            demandForecast = ''

            item = SecondIndexItem()

            item['purchaseIndex1688'] = pIndex1688
            item['supplyIndex'] = supplyIndex
            item['demandForecast'] = demandForecast

            yield item

