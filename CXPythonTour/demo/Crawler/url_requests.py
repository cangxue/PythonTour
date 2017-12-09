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

#=============== 高级用法 ==================
from requests import Request, Session

# 1、会话对象
# session = requests.Session()
# session.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# response = session.get('http://httpbin.org/cookies')
# # print(response.text)
#
# session.auth = ('user', 'pass')
# session.headers.update({'x-test': 'true'})
# response = session.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(response.text)

# response = session.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print(response.text)
# response = session.get('http://httpbin.org/cookies')
# print(response.text)

# with requests.Session() as s:
#     response = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#
# print(response.text)

# 2、请求与响应对象
# response = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
# print(response.headers)
# print(response.request.headers)

# 3、准备的请求
# url = 'https://github.com/timeline.json'
# headers = {'user-agent': 'my-app/0.0.1'}
# payload = {'key1': 'value1', 'key2': 'value2'}
# session = Session()
# req = Request('GET', url,
#               data=payload,
#               headers=headers)
# prepped = session.prepare_request(req)
# resp = session.send(prepped,
#                     stream=False,
#                     verify=True,
#                     proxies=payload,
#                     cert=None,
#                     timeout=10)
# print(resp.status_code)
# print(resp.text)

# 4、SSL证书验证
# requests.get('https://requestb.in')
# print(requests.get('https://github.com', verify=True))
# requests.get('https://github.com', verify='/path/to/certfile')
# session = requests.Session()
# # session.verify = '/path/to/certfile'
# session.verify = True
# response = session.get('https://github.com')
# print(response.text)

# 5、客户端证书
# session = requests.Session()
# session.cert = '/path/client.cert'
# response = requests.get('https://kennethreitz.org', cert='/wrong_path/client.pem')
# print(response.text)

# 6、响应体内容工作流
# tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
# response = requests.get(tarball_url, stream=True)
# # print(response.headers)
# if int(response.headers['Content-Length']) > 0:
#     content = response.content
#     print(content)

# with requests.get('http://httpbin.org/get', stream=True) as response:
#     print(response.text)


# 7、流式上传
# with open('massive-body') as f:
#     response = requests.post('http://some.url/streamed', data=f)
# print(response.text)

# 8、块编码请求
# def gen():
#     yield 'hi'
#     yield 'threre'
# response = requests.post('http://some.url/chunked', data=gen())
# print(response.text)

# 9、POST 多个分块编码的文件
# url = 'http://httpbin.org/post'
# multiple_files=[
#     ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
#     ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))
# ]
# respons = requests.post(url, files=multiple_files)
# print(respons.text)

# 10、事件挂钩
# print_url = 'https://github.com/timeline.json'
# hooks = dict(response=print_url)
# resp = requests.get('http://httpbin.org', hooks=hooks)
# print(resp.text)

# 11、自定义身份验证
# from requests.auth import AuthBase
# class PizzaAuth(AuthBase):
#     def __init__(self, username):
#         self.username = username
#     def __call__(self, r):
#         r.headers['X-Pizza'] = self.username
#         return r
#
# response = requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
# print(response.status_code)

# 12、流式请求
# response = requests.get('http://httpbin.org/stream/20', stream=True)

# for line in response.iter_lines():
#     if line:
#         decoded_line = line.decode('utf-8')
#         print(json.loads(decoded_line))

# if response.encoding is None:
#     response.encoding = 'utf-8'
# for line in response.iter_lines(decode_unicode=True):
#     if line:
#         print(json.loads(line))

# lines = response.iter_lines()
# first_line = next(lines)
# for line in lines:
#     print(line)

# 13、代理
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "http://10.10.1.10:1080",
# }
# # proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}
# # SOCKS
# proxies = {
#     'http': 'socks5://user:pass@host:port',
#     'https': 'socks5://user:pass@host:port'
# }
#
# response = requests.get('http://example.org', proxies=proxies)
# print(response.text)

# 14、HTTP动词
r = requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
if (r.status_code == requests.codes.ok):
    print(r.headers['content-type'])
commit_data = r.json()
print(commit_data)
print(commit_data.keys())


