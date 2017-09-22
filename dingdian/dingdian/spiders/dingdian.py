#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 11:02
# @Author  : huiliu@annoroad.com
# @Descript: 
# @File    : dingdian.py
# @Software: PyCharm
import re
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from dingdian.items import DingdianItem


class Myspider(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['x23us.com']
    bash_url = 'http://www.x23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 2):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)
        # yield Request('http://www.x23us.com/quanben/1', self.parse)

    def parse(self, response):
        # print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')
        max_num = soup.find('div', class_='pagelink').find_all('a')[-1].get_text()
        bashurl = str(response.url)[:-7]
        for num in range(1, int(max_num)+1):
            url = bashurl + '_' + str(num) + self.bashurl
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgclolor='#FFFFFF')
        for td in tds:
            novelname = td.find('a').get_text()
            novelurl = td.find('a')['href']
            yield Request(novelurl, callback=self.get_chaperurl, meta={'name': novelname,
                                                                       'url': novelurl})

    def get_chaperurl(self, response):
        item = DingdianItem()
        item['name'] = str(response.meta['name']).replace('\xa0', '')
        item['novelurl'] = response.meta['url']
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_test()
        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
        name_id = str(bash_url)[-6:-1].replace('/', '')
        item['category'] = str(category).replace('/', '')
        item['author'] = str(author).replace('/', '')
        item['name_id'] = name_id
        print(item)
        yield item
