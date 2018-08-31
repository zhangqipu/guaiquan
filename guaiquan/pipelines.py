# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from guaiquan.items_detail import GuaiquanDetailItem
from guaiquan.items import GuaiquanItem

class GuaiquanPipeline(object):

    def __init__(self):
        dbargs = dict(
            host = '127.0.0.1' ,
            db = 'xiaocaimi',
            user = 'root', #replace with you user name
            passwd = 'Cuo2017c', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        # print (item['head_img_url'])
        if isinstance(item, GuaiquanDetailItem):
            res = self.dbpool.runInteraction(self.update_table, item)
        if isinstance(item, GuaiquanItem):
            res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    def insert_into_table(self, conn, item):
            conn.execute('insert into scrypydata(title, url) values(%s,%s)', (item['title'],item['url']))

    def update_table(self, conn, item):
            conn.execute('update scrypydata set head_img_url = %s where url = %s', (item['head_img_url'],item['url']))
