# -*- coding: utf-8 -*-
import scrapy
from ActiveWish.items import ActivewishItem

class Kuaiyispider1Spider(scrapy.Spider):
    name = 'kuaiyiSpider'
    allowed_domains = ['kuaiyilicai.com']
    start_urls = ['https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1960.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1961.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1962.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1963.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1964.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1965.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1966.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1967.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1968.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1969.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1970.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1971.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1972.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1973.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1974.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1975.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1976.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1977.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1978.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1979.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1980.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1981.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1982.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1983.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1984.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1985.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1986.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1987.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1988.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1989.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1990.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1991.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1992.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1993.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1994.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1995.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1996.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1997.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1998.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/1999.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2000.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2001.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2002.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2003.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2004.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2005.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2006.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2007.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2008.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2009.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2010.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2011.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2012.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2013.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2014.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2015.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2016.html',
                  'https://www.kuaiyilicai.com/stats/global/yearly/g_gdp/2017.html'
                  ]

    def parse(self, response):
        awItems = ActivewishItem()

        title = response.css('div h3::text').extract()
        # datas_tbody = response.css('tbody td::text').extract()
        datas = response.css('tbody tr')
        year = title[0][0:4]

        print(year)

        for data in datas:
            row = data.css('td::text').extract()
            if len(row) == 4:
                awItems['id'] = year + "-" + row[0]
                awItems['sort'] = row[0]
                awItems['country'] = row[1]
                awItems['continent'] = row[2]
                awItems['GDP'] = row[3]
                awItems['year'] = year
            print(row)
            yield awItems

