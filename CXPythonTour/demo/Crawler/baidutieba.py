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
    def __init__(self, baseUrl, seeLZ, floorTag):
        # base链接地址
        self.baseURL = baseUrl
        # 是否只看楼主：1是
        self.seeLZ = '?see_lz=' + str(seeLZ)
        # HTML标签剔除工具类对象
        self.tool = Tool()
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层标号，初始为1
        self.floor = 1
        # 默认标题
        self.defaultTitle = u'百度贴吧'
        # 是否写入楼层分隔符的标记
        self.floorTag = floorTag

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
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            if len(content) > 50:
                contents.append(content)
        return contents

    # 设置文件标题
    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + '.txt', "a")
        else:
            self.file = open(self.defaultTitle + '.txt', 'a')

    # 写入数据
    def writeData(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == 1:
                # 楼层分隔符
                floorLine = '\n 第' + str(self.floor) + u"楼-----------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    # 开始启动
    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print('URL已失效，请重试')
            return
        try:
            print('改帖子共有' + str(pageNum) + '页')
            for i in range(1, int(pageNum)+1):
                print('正在写入第' + str(i) + "页数据")
                page = self.getPage(i)
                contents = self.getContent(page)
                if len(contents) > 0:
                    self.writeData(contents)


        # 出现写入异常
        except IOError as e:
            print('写入异常，原因：' + e.message)
        finally:
            print('写入任务完成')


baseURL = 'http://tieba.baidu.com/p/4083780363'
seeLZ = 1
floorTag = 0
bdtb = BDTB(baseURL, seeLZ, floorTag)
bdtb.start()






