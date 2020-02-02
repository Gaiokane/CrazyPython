import sqlite3
import pygal

# 导入10-5生成的db文件
conn = sqlite3.connect("Chapter_10/10-6/infos.db")
cur = conn.cursor()
# 执行查询
cur.execute("select * from info_tb")
# 该字典以时间为key，以时间内包含的文章数为value
# 用于统计时间下文章数量
date_dict = {}
for art_date in cur:
    # 获取时间
    date = art_date[1]
    # 如果该字典中已有该时间的文章信息，将文章数+1
    if date in date_dict:
        date_dict[date] += 1
    # 否则，说明该时间是第一次统计
    else:
        date_dict[date] = 1

# article_date article_name article_describe

pie = pygal.Pie()

for art_amount in date_dict.keys():
    pie.add(art_amount, date_dict[date])

pie.title = '文章信息'
pie.legend_at_bottom = True
# 输出到图片
pie.render_to_file("Chapter_10/10-6/10-6.svg")