import urllib.request
import http.cookiejar

# urlopen(url,data=None):打开URL对应的资源
# 如果你要能保持客户端多次请求的状态，那么必须借助于cookie，python有个http.cookiejar

# 创建CookieJar对象
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 创建一个Cookie处理器
cookie_proc = urllib.request.HTTPCookieProcessor(cookie_jar)
# 创建OpenerDirector对象，当程序使用OpenerDirector对象来发送多次请求时，
# 它们使用相同的Cookie，因此服务端就可以维持多次访问的状态
opener = urllib.request.build_opener(cookie_proc)

# 用字典代表请求参数
params = {'name': 'qqq', 'pass': 'qk'}

# 此处使用opener的open()的方法
with opener.open('http://127.0.0.1/login.jsp', data=urllib.parse.urlencode(params).encode('UTF-8')) as f:
    print(f.read().decode('UTF-8'))

# 此处使用opener的open()的方法，多次open与服务器建立请求，服务器可根据Cookie来维护它们的状态
# with opener.open('http://127.0.0.1/secret.jsp') as f:
    print(f.read().decode('UTF-8'))
