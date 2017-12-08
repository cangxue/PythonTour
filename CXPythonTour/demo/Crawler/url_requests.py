#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-07
@author: Palesnow

@content: requests获取url信息
@参考资料：http://docs.python-requests.org/zh_CN/latest/index.html

"""

import requests
import json

#=============== 快速上手 ==================
# 1、发送请求
# response = requests.get('https://github.com/timeline.json')
# response = requests.post('http://httpbin.org/post')
# response = requests.put('http://httpbin.org/put')
# response = requests.delete('http://httpbin.org/delete')
# response = requests.head('http://httpbin.org/get')
# response = requests.options('http://httpbin.org/ge')
# print(response.text)
# print(response.json())

# 2、传递URL参数
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# url = 'http://httpbin.org/get'
# response = requests.get(url, params=payload)
# print(response.url)
# print(response.text)

# 3、响应内容
# response = requests.get('https://github.com/timeline.json')
# print(response.text)
# print(response.encoding)
# response.encoding = 'ISO-8859-1'
# print(response.text)
# print(response.encoding)
#
# # 二进制响应内容
# print(response.content)
#
# # JSON响应内容
# print(response.json())
#
# # 原始响应内容
# response = requests.get('https://github.com/timeline.json', stream=True)
# print(response.raw)
# print(response.raw.read())

# 4、定制请求头
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# response = requests.get(url, headers=headers)
# print(response.text)

# 5、更加复杂的POST请求
# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('http://httpbin.org/post', data=payload)
# print(response.text)
#
# payload = (('key1', 'value1'), ('key1', 'value2'))
# response = requests.post('http://httpbin.org/post', data=payload)
# print(response.text)

# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# response = requests.post(url, data=json.dumps(payload))
# print(response.text)
#
# response = requests.post(url, json=payload)
# print(response.text)

# 6、POST一个多部分编码(Multipart-Encoded)的文件¶
# url = 'http://httpbin.org/post'
# files = {'file': open('url_urllib.py', 'rb')}
#
# # 显式地设置文件名，文件类型和请求头
# files = {'file': ('url_urllib.py', open('url_urllib.py', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
#
# # 发送作为文件来接收的字符串
# files = {'file': ('url_urllib.py', 'some,data,to,send\nanother,row,to,send\n')}
# response = requests.post(url, files=files)
# print(response.text)

# 7、响应状态码
# response = requests.get('http://httpbin.org/get')
# print(response.status_code)
# print(response.status_code == requests.codes.ok)
#
# bad_response = requests.get('http://httpbin.org/status/404')
# print(bad_response.status_code)
# print(bad_response.raise_for_status())

# 8、响应头
# response = requests.get('http://httpbin.org/get')
# print(response.headers)
# print(response.headers.get('content-type'))

# 9、Cookie
# url = 'http://example.com/some/cookie/setting/url'
# response = requests.get(url)
# print(response.text)
# print(response.cookies)

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# response = requests.get(url, cookies=cookies)
# print(response.text)
#
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# response = requests.get(url, cookies=jar)
# print(response.text)

# 10、重定向与请求历史
# response = requests.get('http://github.com')
# print(response.url)
# print(response.status_code)
# print(response.history)
#
# # 禁用重定向处理
# response = requests.get('http://github.com', allow_redirects=False)
# print(response.url)
# print(response.status_code)
# print(response.history)

# # 启用重定向
# response = requests.head('http://github.com', allow_redirects=True)
# print(response.url)
# print(response.status_code)
# print(response.history)

# 11、超时
# response =

# 12、错误与异常
'''
遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。

如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。

若请求超时，则抛出一个 Timeout 异常。

若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。

所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。
'''

