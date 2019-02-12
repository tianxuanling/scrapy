# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import uuid
import pymysql

class ActivewishPipeline(object):
    def __init__(self):
        self.client = pymysql.connect(
            host='192.168.77.100',
            port=30653,
            user='root',  # 使用自己的用户名
            passwd='shanhong',  # 使用自己的密码
            db='txl-scrapy',  # 数据库名
            charset='utf8'
        )
        self.cur = self.client.cursor()


    def process_item(self, item, spider):
        sql = 'insert into scrapy_gdp(id,sort,country,continent,GDP,year,createusercode,createusername,createtime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,sysdate())'
        lis = (item['id'], item['sort'], item['country'], item['continent'], item['GDP'], item['year'], '19860314', 'txl')
        self.cur.execute(sql, lis)
        self.client.commit()
        #self.cur.close()
        #self.client.close()
        return item
