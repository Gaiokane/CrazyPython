import urllib.parse

# urlparse()：用于解析URL字符串，将URL字符串分解成各部分。返回值为ParseResult（tuple的子类）
# urlunparse()：将URL各部分（ParseResult或tuple）恢复成URL字符串

s = 'https://umaru.moe:80/index.php;abc?name=Gaiokane#myfrag'
# 解析URL字符串
r = urllib.parse.urlparse(s)
print(r)  # ParseResult对象
# ParseResult是tuple的子类
print('协议', r.scheme, r[0])
print('位置', r.netloc, r[1])
print('资源路径', r.path, r[2])
print('参数', r.params, r[3])
print('查询字符串', r.query, r[4])
print('fragment', r.fragment, r[5])

print('-'*50)

# 元组
tu = ('http', 'h5.umaru.moe:80', '/index1.php',
      'qqq', 'name=gaiokane', 'myfrag')

# 恢复查询字符串
print(urllib.parse.urlunparse(tu))

print('-'*50)

# ——————————————————————————————————————————————————————

# parse_qs()、parse_qsl()：用于解析查询字符串，得到字典或列表
# urlencode()：将列表或字典恢复成查询字符串

# 查询字符串的格式为：key=value，多个keyvalue对之间用&隔开
qs = 'name=qk&name=Gaiokane&age=24&height=173'

print(urllib.parse.parse_qs(qs))  # 返回字典
print(urllib.parse.parse_qsl(qs))  # 返回列表

# 已有列表
lt = [('name', 'qk'), ('name', 'Gaiokane'), ('age', '24')]

# 将列表恢复成查询字符串
print(urllib.parse.urlencode(lt))

# 已有字典
query_dict = {'name': 'qk', 'age': '24', 'height': '173'}
# 将列表恢复成查询字符串
print(urllib.parse.urlencode(query_dict))