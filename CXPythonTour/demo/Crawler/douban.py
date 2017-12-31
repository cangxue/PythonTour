#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-28
@author: Palesnow

@content: 豆瓣爬取
          1、获取排行榜
          2、获取影评

"""

import requests
import re

class DOUBAN:
    # 初始化
    def __init__(self, baseUrl):
        self.baseURL = baseUrl
    # 获取数据
    def getPage(self, pageNum):
        try:
            url = self.baseURL + 'start=' + str(pageNum) + '&type=T'
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            return None
        except requests.RequestException as e:
            print(e)

    # 解析处理数据
    def getContent(self, page):
        pattern = re.compile('<table width=".*?<div class="pl2">.*?>(.*?)</a>.*?class="pl">(.*?)</p>'
                             + '.*?<span class="rating_nums">(.*?)</span>.*?class="pl">(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            yield {
                'title': item[0].split("/")[0].strip(),
                'actor': item[1].split("/"),
                'average': item[2],
                'content': item[3],
            }

    # 开始接口
    def start(self):
        for pageIndex in range(0, 2):
            page = self.getPage(pageIndex)
            print("===============================第%s页数据======================" % pageIndex)
            for item in self.getContent(page):
                print(item)

url = 'https://movie.douban.com/tag/2016?'
douban = DOUBAN(url)
douban.start()







