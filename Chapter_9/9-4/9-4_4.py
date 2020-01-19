import pygal
import random

year_data = [str(i) for i in range(2011, 2020)]
banana_data = [random.randint(20, 40) * 1000 for i in range(1, 10)]
apple_data = [random.randint(35, 60) * 1000 for i in range(1, 10)]
# 创建图（pygal.Dot代表点图）
graph = pygal.Dot()
graph.title = '香蕉与苹果历年的销量分析'

# 添加数据
graph.add('香蕉的历年销量', banana_data)
graph.add('苹果的历年销量', apple_data)

# 设置X的坐标数据
graph.x_labels = year_data
graph.x_title = '年份'
#graph.y_title = '销量（吨）'

# 设置x轴的标签旋转多少度
graph.y_label_rotation = 45
# 设置将图例放在下面
#graph.legend_at_bottom = True
# 设置四周的页边距，也可使用margin_bottom、margin_top、margin_left、margin_right分别设置
graph.margin = 35
# 显示y轴的网格线
graph.show_y_guides = False
# 显示x轴的网格线
graph.show_x_guides = True

# 输出到图片
graph.render_to_file("Chapter_9/9-4/9-4_4.svg")
