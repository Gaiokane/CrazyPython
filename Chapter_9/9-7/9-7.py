import urllib.request
import re
import datetime
import pygal


def get_html(city, year, month):
    url = 'https://m.tianqi.com/lishi/%s/%s%s.html' % (city, year, month)
    request = urllib.request.Request(url)
    # 设置User-Agent头，避免产生403错误
    #request.add_header('User-Agent', 'Chrome/79.0.3945.130')
    request.add_header('User-Agent', 'Mozilla/5.0')
    return urllib.request.urlopen(request).read().decode('UTF-8')
# print(get_html('suzhou','2020','01'))


dates, highs, lows = [], [], []
city = 'suzhou'
year = '2019'
months = ['%02d' % i for i in range(1, 13)]
#months = ['01']
# 定义一个开始日期，用于判断数据是否缺少某天
prev_day = datetime.datetime(2018, 12, 31)

for month in months:
    # 下载网页源代码
    html = get_html(city, year, month)
    # 将网页源代码的空格去掉
    nospace_text = ''.join(html.split())
    # print(nospace_text)
    # 定义包含全部天气数据的div元素所对应的正则表达式

    pattern = re.compile(
        '<divclass="weatherbox">(.*?)</div><divclass="clearline1">')
    div_list = re.findall(pattern, nospace_text)
    # print(div_list[0])
    # 定义包含每日天气对于的dl元素所对应的正则表达式
    pattern1 = re.compile('<dlclass="table_day15">(.*?)</dl>')
    dls = re.findall(pattern1, div_list[0])
    # print(len(dls))
    # 再次遍历dls去获取每天的数据
    for dl in dls:
        # 日期对应正则表达式
        date_pattern = re.compile('<ddclass="date">(.*?)</dd>')
        date_dd = re.findall(date_pattern, dl)
        # 生成日期格式字符串
        d_str = year + "/" + date_dd[0][0:5]

        # 气温信息对应正则表达式
        temp_pattern = re.compile('<ddclass="txt2">(.*?)</dd>')
        temp_dd = re.findall(temp_pattern, dl)
        # print(temp_dd)

        # 最低气温信息对应正则表达式
        low_pattern = re.compile('^(.*?)~')
        low_li = re.findall(low_pattern, temp_dd[0])
        # print(low_li)

        # 最高气温信息对应正则表达式
        high_pattern = re.compile('<b>(.*?)</b>')
        high_li = re.findall(high_pattern, temp_dd[0])
        # print(high_li)

        try:
            cur_day = datetime.datetime.strptime(d_str, '%Y/%m/%d')
            # 得到最低气温和最高气温
            low = int(low_li[0])
            high = int(high_li[0])
        except ValueError:
            print(cur_day, '温度数据格式有错')
        else:
            # 数据清洗，判断是否差某一天
            diff = cur_day - prev_day

            # 如果两个日期之间的差值不是一天，说明丢失了数据
            if diff != datetime.timedelta(days=1):
                print('在%s之前丢失了%d天的数据' % (d_str, diff.days-1))

            dates.append(d_str)
            lows.append(low)
            highs.append(high)
            prev_day = cur_day

# 创建图（pygal.Line代表折线图）
bar = pygal.Line()
bar.title = '苏州%s年的气温分析' % year

# 添加数据
bar.add('最低气温', lows)
bar.add('最高气温', highs)

bar.x_labels = dates
# 设置x轴的主刻度
bar.x_labels_major = dates[::30]
# 设置不显示x轴上的小刻度（避免密密麻麻）
bar.show_minor_x_labels = False
bar.x_title = '日期'
bar.y_title = '气温（℃）'

# 设置x轴的标签旋转多少度
bar.x_label_rotation = 45
# 设置将图例放在下面
bar.legend_at_bottom = True
# 显示y轴的网格线
bar.show_y_guides = True
# 显示x轴的网格线
bar.show_x_guides = False

# 输出到图片
bar.render_to_file("Chapter_9/9-7/9-7.svg")
