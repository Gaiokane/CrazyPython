接10-3

1.改写pipelines
Chapter_10\10-7\UmarumoeSpider\UmarumoeSpider\pipelines.py

2.配置settings
Chapter_10\10-7\UmarumoeSpider\UmarumoeSpider\settings.py
42行
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

67行
ITEM_PIPELINES = {
    'UmarumoeSpider.pipelines.UmarumoespiderPipeline': 300,
}

3.运行
cd Chapter_10\10-7\UmarumoeSpider\UmarumoeSpider
scrapy crawl article_info

#通过Item定义感兴趣的数据项
#定义Spider爬取数据
#使用pipeline处理数据