import sqlite3

#1.打开数据库连接
#SQLite它是一个没有后台进程的数据库，磁盘上一个文件就可对应SQLite数据库
conn = sqlite3.connect("Chapter_7/7-2/test.db")

#2.打开游标
c = conn.cursor()

#3.使用游标的execute方法执行任意SQL语句（DDL）
#SQLite可以忽略数据列的类型
'''
    create table user_tb(
        _id integer primary key autoincrement,
        name,
        pass,
        age)
'''
c.execute('''
    create table user_tb(
        _id integer primary key autoincrement,
        name text,
        pass text,
        age integer)
''')

#3.使用游标的execute方法执行任意SQL语句（DDL）
c.execute('''
    create table order_tb(
        _id integer primary key autoincrement,
        item_name text,
        item_price real,
        item_number integer,
        user_id integer,
        foreign key(user_id) references user_tb(_id))
''')

#4.关闭游标
c.close()

#5.关闭数据库连接
conn.close()