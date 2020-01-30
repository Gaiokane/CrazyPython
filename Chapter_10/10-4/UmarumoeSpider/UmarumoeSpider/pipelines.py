# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class UmarumoespiderPipeline(object):
    def __init__(self):
        #初始化要写入的JSON文件
        self.json_file = open('infos.json','wb+')
        self.json_file.write('\n'.encode('utf-8'))

    #该方法的item参数就是蜘蛛yield所返回的item对象
    def process_item(self, item, spider):
        """ #此处只是将爬取得到的信息打印在控制台
        print('文章时间',item['article_date'])
        print('文章名字',item['article_name'])
        print('文章描述',item['article_describe']) """
        #将每个item对象转化成一个json字符串
        text = json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.json_file.write(text.encode('utf-8'))
    
    #当蜘蛛关闭时（自动调用close_spider方法），程序要关闭文件
    def close_spider(self,spider):
        print('-------关闭文件-------')
        self.json_file.seek(-2,1)
        self.json_file.write('\n'.encode('utf-8'))
        self.json_file.close()