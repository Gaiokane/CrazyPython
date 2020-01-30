# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class UmarumoespiderPipeline(object):
    #该方法的item参数就是蜘蛛yield所返回的item对象
    def process_item(self, item, spider):
        #此处只是将爬取得到的信息打印在控制台
        print('文章时间',item['article_date'])
        print('文章名字',item['article_name'])
        print('文章描述',item['article_describe'])
