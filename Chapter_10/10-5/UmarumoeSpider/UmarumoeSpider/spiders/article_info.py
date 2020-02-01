# -*- coding: utf-8 -*-
import scrapy
from UmarumoeSpider.items import UmarumoespiderItem


class ArticleInfoSpider(scrapy.Spider):
    # 蜘蛛的名字
    name = 'article_info'
    # 定义蜘蛛只爬取哪些域名
    allowed_domains = ['umaru.moe']
    # 从哪个页面开始爬
    start_urls = ['http://umaru.moe/']

    # 该response就代表Scrapy下载器所获取的目标的响应
    # 和shell调试中response对象完全一样
    def parse(self, response):
        # site-main下包含多个文章信息
        for article_info in response.xpath('//div[@class="content-area"]/main[@class="site-main"]'):
            # 为每个文章创建一个Item对象
            item = UmarumoespiderItem()

            # 获取包含文章信息的div
            item['article_date'] = article_info.xpath(
                '//header/div/a/time[1]/text()').extract()
            item['article_name'] = article_info.xpath(
                '//header/h3/a/text()').extract()
            item['article_describe'] = article_info.xpath(
                '//div[@class="entry-content"]/p/text()').extract()

            # 返回得到的item对应生成器
            yield item

        """ #处理分页
        new_links = response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract()
        if new_links and len(new_links) > 0:
            new_links = new_links[0]
            #指定再次发送请求，并使用self.parse来处理服务器响应
            yield scrapy.Request('https://www.zhipin.com' + new_links, callback=self.parse) """
