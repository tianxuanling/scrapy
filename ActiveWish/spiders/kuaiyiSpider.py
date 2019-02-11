# -*- coding: utf-8 -*-
import scrapy
from ActiveWish.items import ActivewishItem

class Kuaiyispider1Spider(scrapy.Spider):
    name = 'kuaiyiSpider'
    allowed_domains = ['kuaiyilicai.com']
    start_urls = ['https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1960.html']

    def parse(self, response):
        awItems = ActivewishItem()

        title = response.css('div h3::text').extract()
        datas_tbody = response.css('tbody td::text').extract()

        awItems['sort'] = response.css('tbody td::text').extract()[2]
        awItems['country'] = response.css('tbody td::text').extract()[3]
        awItems['continent'] = response.css('tbody td::text').extract()[4]
        awItems['GDP'] = response.css('tbody td::text').extract()[5]
        awItems['year'] = title[0][0:4]

        print(title[0][0:4])
        print(datas_tbody)

        return awItems
