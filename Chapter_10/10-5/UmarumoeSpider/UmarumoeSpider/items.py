# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UmarumoespiderItem(scrapy.Item):
    #文章时间
    article_date = scrapy.Field()
    #文章名字
    article_name = scrapy.Field()
    #文章描述
    article_describe = scrapy.Field()
    pass
