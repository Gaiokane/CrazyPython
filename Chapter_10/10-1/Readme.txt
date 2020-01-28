#下载Twisted包
https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
d:
cd D:\python-program\GitHub\CrazyPython\Chapter_10\10-1
#安装Twisted
pip3 install Twisted-19.10.0-cp37-cp37m-win_amd64.whl
#安装scrapy
pip3 install scrapy
#创建Scrapy项目
scrapy startproject ZhipinSpider

#项目的总配置文件，通常无需修改
scrapy.cfg
#项目Python模块，程序将从此处导入Python代码
ZhipinSpider/

Scrapy引擎流程：
Scrapy引擎调用调度中间件，调度器向互联网发送请求，
Scrapy引擎调用下载中间件，下载器从互联网获取数据，
Scrapy引擎调用蜘蛛中间件，蜘蛛从响应中筛选数据，
Scrapy引擎将筛选出的数据封装成Item并传给Pipeline
#从调度器开始向互联网发送请求，下载器从互联网上得到数据，将响应传给蜘蛛，蜘蛛从响应中获取指定数据，Scrapy将提取出的数据封装成Item并传给Pipeline

调度器：该组件由Scrapy框架实现
下载器：该组件由Scrapy框架实现
蜘蛛：该组件由开发者实现
Pipeline：该组件由开发者实现