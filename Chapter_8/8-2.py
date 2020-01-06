import urllib.request

# urlopen(rul, data=None)：打开URL对应的资源

# 打开网络资源后，该资源就像一个文件
with urllib.request.urlopen('https://umaru.moe/') as f:
    print(f.read(777).decode('UTF-8'))

# 用字典代表请求参数
params = {'name': 'Gaiokane', 'password': 'qk'}
# GET请求参数，只需要添加到URL之后即可
with urllib.request.urlopen('https://umaru.moe/get.php?%s' % urllib.parse.urlencode(params)) as f:
    print(f.read().decode('UTF-8'))

# 用字典代表请求参数
params = {'name': 'Gaiokane', 'password': 'qk'}
# POST请求参数，用data参数来指定
with urllib.request.urlopen('https://umaru.moe/post.php?', data=urllib.parse.urlencode(params).encode('UTF-8')) as f:
    print(f.read().decode('UTF-8'))

# 定义需要put的请求参数
params = 'put数据'.encode('UTF-8')
# 如果要发送PUT/PATCH/DELETE等请求，需要创建Request对象
req = urllib.request.Request(
    url='https://umaru.moe/put', data=params, method='PUT')
# 有了Request对象之后，用urlopen打开该对象即可
with urllib.request.urlopen(req) as f:
    print(f.read().decode('UTF-8'))