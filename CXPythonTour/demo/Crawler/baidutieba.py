#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-14
@author: Palesnow

@content: 百度贴吧爬取
@参考资料：http://wiki.jikexueyuan.com/project/python-crawler-guide/post.html

"""

import requests
import re

# 处理页面标签类
class Tool:
    # 去除img标签，7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加两空格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()

# 百度贴吧爬虫类
class BDTB:
    # 初始化
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()

    # 获取某页帖子的代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            response = requests.get(url)
            return response.text
        except requests.RequestException as e:
            print(e)

    # 获取帖子标题
    def getTitle(self, page):
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            # 如果存在，则返回标题
            return result.group(1).strip()
        else:
            return None

    # 获取帖子页数
    def getPageNum(self, page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            # 如果存在，则返回页数
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        floor = 1
        for item in items:
            print(floor, u'楼------------------------------------------------------')
            print(self.tool.replace(item))
            floor += 1





baseURL = 'http://tieba.baidu.com/p/4083780363'
bdtb = BDTB(baseURL, 1)

print(bdtb.getContent(bdtb.getPage(1)))


