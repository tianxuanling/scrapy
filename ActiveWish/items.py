# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ActivewishItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    sort = scrapy.Field()
    country = scrapy.Field()
    continent = scrapy.Field()
    GDP = scrapy.Field()
    year = scrapy.Field()
    pass
