#以下命令均在cmd下运行

#爬取数据
scrapy shell -s USER_AGENT='Mozilla/5.0' https://umaru.moe/

#查看response的方法，主要方法有两个：xpath、css，分别使用这两种方法提取数据
dir(response)

#<h3 class="entry-title">
response.xpath('//h3[@class="entry-title"]')
response.xpath('//h3[@class="entry-title"]/a/text()').extract()

#<h3 class="entry-title">
response.css('h3.entry-title>a').extract()