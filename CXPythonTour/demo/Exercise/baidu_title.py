import re
from urllib import request

#爬虫爬取百度首页内容
data = request.urlopen("http://www.baidu.com").read().decode()

#分析网页，确定正则表达式
pat = r'<title>(.*?)</title>'

result = re.search(pat, data)
print(result)

result.group()