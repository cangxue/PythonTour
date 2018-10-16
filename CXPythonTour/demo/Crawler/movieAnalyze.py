
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2018-05-25
@author: Palesnow

@content: 影评分析
          1、抓取网页数据
          2、清理数据
          3、用词云进行展示

"""

from urllib import request

# 抓取网页数据
resp = request.urlopen('https://movie.douban.com/nowplaying/hangzhou/')
html_date = resp.read().decode('utf-8')
print(html_date)
