import urllib.request,re
import datetime

def get_html(city,year,month):
    url='https://m.tianqi.com/lishi/%s/%s%s.html' % (city,year,month)
    request = urllib.request.Request(url)
    #设置User-Agent头，避免产生403错误
    request.add_header('User-Agent','Chrome/79.0.3945.130')
    return urllib.request.urlopen(request).read().decode('UTF-8')
#print(get_html('suzhou','2020','01'))

dates,highs,lows=[],[],[]
city='suzhou'
year='2019'
#months=['%02d'%i for i in range(1,13)]
months=['01']
#定义一个开始日期，用于判断数据是否缺少某天
prev=datetime.datetime(2017,12,31)

for month in months:
    #下载网页源代码
    html=get_html(city,year,month)
    #将网页源代码的空格去掉
    nospace_text = ''.join(html.split())
    #print(nospace_text)
    #定义包含全部天气数据的div元素所对应的正则表达式
    
    pattern = re.compile('<divclass="weatherbox">(.*?)</div><divclass="clearline1">')
    div_list=re.findall(pattern,nospace_text)
    #print(div_list[0])
    #定义包含每日天气对于的dl元素所对应的正则表达式
    pattern1 = re.compile('<dlclass="table_day15">(.*?)</dl>')
    dls=re.findall(pattern1,div_list[0])
    #print(len(dls))
    #再次遍历dls去获取每天的数据