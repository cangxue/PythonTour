# coding=utf-8

"""
Created on 2017-12-07
@author: Palesnow

@content: 获取天气信息

"""


import requests
import bs4

class Weather:
    # 初始化
    def __init__(self):
        self.baseURL = 'http://www.weather.com.cn/weather/'  # 七日天气
        self.city_id = '101010200'  # 默认北京/海淀

    # 请求URL中的html信息
    def get_html(self):
        # 封装请求
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            'ContentType': 'text/html; charset=utf-8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
        }

        try:
            url = self.baseURL + self.city_id + '.shtml'
            html_content = requests.get(url, headers=headers, timeout=30)
            html_content.raise_for_status()
            html_content.encoding = 'utf-8'
            return html_content.text
        except:
            return '请求失败'

    # 获取爬取内容
    def get_content(self):
        # 抓取页面天气数据
        html = self.get_html()
        soup = bs4.BeautifulSoup(html, 'html.parser')

        # 获取城市名称
        city = soup.find('div', class_='crumbs fl').find_all('a')
        citys = []
        for content in city:
            citys.append(content.text)
        city_name = '>'.join(citys)

        district = soup.find('div', class_='crumbs fl').find_all('span')
        district_name = district[len(district) - 1].text

        city_name = city_name + '>' + district_name

        print(city_name)

        # 获取天气信息
        weather_list = []

        content_ul = soup.find('ul', class_='t clearfix').find_all('li')

        for content in content_ul:
            try:
                weather = {}
                weather['day'] = content.find('h1').text
                weather['weather'] = content.find('p', class_='wea').text
                weather['temperature'] = content.find('p', class_='tem').span.text + '/' + \
                                         content.find('p', class_='tem').i.text
                weather_list.append(weather)
            except:
                print('查询不到')

        print(weather_list)


# 北京天气获取
weather = Weather()
weather.get_content()




