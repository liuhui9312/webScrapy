#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 11:17
# @Author  : huiliu@annoroad.com
# @Descript: 
# @File    : pharmgkb.py
# @Software: PyCharm
import scrapy
import requests
import json
import pandas as pd
from scrapy.http import Request
from scrapy.selector import Selector
from gkb_spider.items import GkbSpiderItem
from gkb_spider import settings


login_url = settings.LOGIN_URL
userid = settings.USERID
password = settings.PASSWORD
drugs_list = settings.DRUGS_LIST
indexs = settings.indexs

class Myspider(scrapy.Spider):
    name = 'gkb_spider'
    allowed_domains = ['pharmgkb.org']
    formdata = {
        "email": userid,
        "password": password
    }
    heads = dict(referer=login_url)
    session_requests = requests.session()
    drugs = pd.read_csv(drugs_list, sep='\t')
    drugs = list(drugs.ix[:, 0])
    checkurl = 'https://api.pharmgkb.org/v1/site/page/variantAnnotations/{}?view=min'

    def start_requests(self):
        return [scrapy.FormRequest(url=login_url,
                                   meta={'cookiejar': 1},
                                   headers=self.heads,
                                   formdata=self.formdata,
                                   callback=self.check_url,
                                   method='POST')]

    def check_url(self, response):
        print('login success!')
        count = 0
        for drug in self.drugs:
            my_url = self.checkurl.format(drug)
            # print(my_url)
            if count % 100 == 0:
                pr = round(count/len(self.drugs)*100)
                print('#'*pr+'_'*(100-pr)+'+++{}%'.format(str(pr)))
                count += 1
            elif count == len(self.drugs) - 1:
                print('#'*100+'+++finished !')
            yield Request(url=my_url,
                          meta={'cookiejar': response.meta['cookiejar'], 'pa_id': drug},
                          headers=dict(referer=my_url),
                          callback=self.parse)

    def parse(self, response):
        # response.encoding = 'gbk'
        sel = response
        mydat = json.loads(sel.text)
        annotations = mydat['data']['variantAnnotations']
        pa_id = response.meta['pa_id']
        items = GkbSpiderItem()
        print('{0} length of annotations : {1}'.format(pa_id, len(annotations)))
        items['pa_id'] = pa_id
        for key in indexs:
            items[key] = {}
        if len(annotations):
            # indexs = list(annotations[0].keys())
            # items['pa_id'] = pa_id
            # for key in indexs:
            #     items[key] = {}
            num = 0
            for annotation in annotations:
                for key in indexs:
                    items[key][num] = ''
                    if key not in annotation.keys():
                        items[key][num] = None
                        continue
                    if isinstance(annotation[key], (int, str)):
                        items[key][num] = str(annotation[key])
                    if isinstance(annotation[key], list):
                        for tp in annotation[key]:
                            if isinstance(tp, dict):
                                items[key][num] += '{},'.format(tp['text'])
                            elif isinstance(tp, str):
                                items[key][num] += '{},'.format(tp)
                            else:
                                print('{} type error!'.format(str(tp)))
                num += 1
            items['num'] = str(len(annotations))
            # print(items)
            # print('return items!!!!!')
            # yield items
        else:
            # print('return None!!!!!')
            items['num'] = 'null'
        yield items
