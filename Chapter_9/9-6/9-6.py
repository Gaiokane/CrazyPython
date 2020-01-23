import json
import pygal

with open('Chapter_9/9-6/gdp_json.json', 'r') as f:
    # load JSON数据返回的是列表或字典
    gdp_data = json.load(f)

# print(gdp_data)
# print(gdp_data[0])

# 只分析如下5个国家的GDP
country_names = ['中国', '美国', '日本', '俄罗斯', '加拿大']
country_codes = ['CHN', 'USA', 'JPN', 'RUS', 'CAN']
# key是年份，value是该年的GDP值
country_gdps = [{}, {}, {}, {}, {}]

for gdp_item in gdp_data:
    for i, country in enumerate(country_codes):
        if gdp_item['Country Code'] == country:
            year = gdp_item['Year']
            # 只处理2001~2016年的数据
            if 2000 < year < 2017:
                country_gdps[i][year] = gdp_item['Value']
# print(country_gdps)

# 转换pygal所需要的格是
country_gdp_list = [[], [], [], [], []]
x_data = range(2001, 2017)
for i in range(len(country_gdp_list)):
    for year in x_data:
        # 除以10的8次方，单位为亿
        country_gdp_list[i].append(country_gdps[i][year]/1e8)

# 创建图
bar = pygal.Bar()
bar.title = '各国历年GDP对比图'

# 添加数据
for i, country_name in enumerate(country_names):
    bar.add(country_name, country_gdp_list[i])

bar.x_labels = x_data
bar.x_title = '年份'
bar.y_title = 'GDP（亿）'

# 设置x轴的标签旋转多少度
bar.x_label_rotation = 45
# 设置将图例放在下面
bar.legend_at_bottom = True
# 隐藏y轴的网格线
bar.show_y_guides = True
# 显示x轴的网格线
bar.show_x_guides = False

# 输出到图片
bar.render_to_file("Chapter_9/9-6/9-6.svg")
