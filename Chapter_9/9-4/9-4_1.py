import pygal
# 2018年8月编程语言的市场份额
data = {'Java': 0.16881, 'C': 0.14996, 'C++': 0.07471, 'Python': 0.06992,
        'VB.net': 0.04762, 'C#': 0.03541, 'PHP': 0.02925, 'JavaScript': 0.02411,
        'SQL': 0.02316, 'Assembly language': 0.01409, '其他': 0.36326}

# pygal.Pie代表饼图
graph = pygal.Pie()
for k in data.keys():
    graph.add(k, data[k])
graph.title = '2018年8月编程语言的市场份额'
graph.legend_at_bottom = True

graph.render_to_file("Chapter_9/9-4/9-4_1.svg")
