#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-07
@author: Palesnow

@content: 使用urllib获取url信息
@参考资料：http://www.jianshu.com/p/d4ebace4ddcf

"""

from urllib import request, parse

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 1、基本方法
url = 'http://www.baidu.com'
response = request.urlopen(url)
print('code: %s  url: %s' % (response.getcode(), response.geturl()))
print('info: %s' % response.info())
page = response.read()
page = page.decode('utf-8')
# print(page)

# 2、使用Request
req = request.Request(url)
page = request.urlopen(req).read()
# print(page.decode('utf-8'))

# 3、POST
url = 'http://www.lagou.com/jobs/positionAjax.json?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,ja;q=0.4,en;q=0.2',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive',
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python'
}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)
page = request.urlopen(req).read()
# print(page.decode('utf-8'))

# 4、GET
values = {}
values['username'] = '123456@qq.com'
values['password'] = '123456'
data = parse.urlencode(values)
url = 'http://passport.csdn.net/account/login'
geturl = url + '?' + data
print(geturl)
req = request.Request(geturl)
response = request.urlopen(req)
# print(response.read())

# 5、使用代理
url = 'http://www.baidu.com'
proxy = request.ProxyHandler({'http': '5.22.195.215:80'})  # 设置proxy
opener = request.build_opener(proxy)  # 挂载opener
request.install_opener(opener)  # 安装opener
page = opener.open(url).read()
print(page.decode('utf-8'))
