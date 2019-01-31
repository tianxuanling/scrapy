# -*- coding: utf-8 -*-
import scrapy


class Kuaiyispider1Spider(scrapy.Spider):
    name = 'kuaiyiSpider'
    allowed_domains = ['kuaiyilicai.com']
    start_urls = ['https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1960.html']

    def parse(self, response):
        datas_thead = response.css('table th::text').extract()
        datas_tbody = response.css('tbody td::text').extract()


        print(datas_thead)
        print(datas_tbody)

        pass
