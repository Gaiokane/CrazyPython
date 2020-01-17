# 安装pygal（命令行执行）
# pip3 install pygal

# 成功安装pygal后，可通过pydoc查看pygal相关文档
# python -m pydoc -p 8899

import pygal

year_data = [str(i) for i in range(2011, 2020)]
java_data = [17.89, 18.29, 20.45, 19.28, 20.35, 21.23, 19.98, 20.24, 19.56]
python_data = [4.89, 4.29, 4.45, 4.28, 5.35, 6.23, 5.98, 6.24, 6.56]
# 创建图（pygal.HorizontalLine代表水平折线图）
bar = pygal.HorizontalLine()
bar.title = 'Java与Python历年的市场份额'

# 添加数据
bar.add('Java市场份额', java_data)
bar.add('Python市场份额', python_data)

#对于水平柱状图，x_labels其实是设置Y轴的坐标
bar.x_labels = year_data
bar.y_title = '年份'
bar.x_title = '市场份额（百分比）'

# 设置x轴的标签旋转多少度
bar.x_label_rotation = 45
# 设置将图例放在下面
bar.legend_at_bottom = True
# 设置四周的页边距，也可使用margin_bottom、margin_top、margin_left、margin_right分别设置
bar.margin = 35
# 显示y轴的网格线
bar.show_y_guides = True
# 显示x轴的网格线
bar.show_x_guides = True

# 输出到图片
bar.render_to_file("Chapter_9/9-2/9-2_3.svg")
