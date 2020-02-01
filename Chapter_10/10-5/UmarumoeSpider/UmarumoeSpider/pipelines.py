# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class UmarumoespiderPipeline(object):
    def __init__(self):
        # 连接数据库
        self.conn = sqlite3.connect("infos.db")
        # 打开游标
        self.c = self.conn.cursor()
        # 打开连接后，如果数据库中没有表，建立数据库
        self.c.execute('create table if not exists info_tb('
                       + 'id integer primary key autoincrement,'
                       + 'article_date,'
                       + 'article_name,'
                       + 'article_describe)')

    # 该方法的item参数就是蜘蛛yield所返回的item对象
    def process_item(self, item, spider):
        self.c.execute('insert into info_tb values(null, ?, ?, ?)',
                       (item['article_date'], item['article_name'], item['article_describe']))
        self.conn.commit()

    # 当蜘蛛关闭时（自动调用close_spider方法），程序要关闭数据库资源
    def close_spider(self, spider):
        print('-------关闭数据库资源-------')
        self.c.close()
        self.conn.close()
