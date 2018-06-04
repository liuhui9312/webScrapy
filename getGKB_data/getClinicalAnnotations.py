#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/19 9:54
# @Author  : huiliu@annoroad.com
# @Descript: 
# @File    : getClinicalAnnotations.py
# @Software: PyCharm
import requests
import json
import pandas as pd
import time

USERID = "##########3@163.com"
PASSWORD = "#########"
LOGIN_URL = "https://api.pharmgkb.org/v1/auth/oauthSignIn"
# heads = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                        'AppleWebKit/537.36 (KHTML, like Gecko) '
#                        'Chrome/60.0.3112.113 Safari/537.36'}
pp = 'https://api.pharmgkb.org/v1/site/page/variantAnnotations/{}?view=min'
pc = 'https://api.pharmgkb.org/v1/site/page/clinicalAnnotations/{}?view=base'


def get_session():
    session_requests = requests.session()
    # Create payload
    payload = {
        "email": USERID,
        "password": PASSWORD
    }
    # Perform login
    result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))
    # scrapy data
    if result.status_code == 200:
        return session_requests
    else:
        return None


def scrap_data():
    session_requests = get_session()
    if not session_requests:
        print('#######login failed#########')
        exit()
    else:
        print('#######login successful######')
    dfi = open('D:/develop/webScrapy/autoLogin/total_annotation_result1.txt', 'w')
    drugs = pd.read_csv('D:/develop/webScrapy/autoLogin/drugs.tsv', sep='\t')
    drugs_list = list(drugs.ix[:, 0])
    indexs = []
    num = 0
    for drug in drugs_list[0:5]:
        drugs_url = pp.format(drug)
        print(drugs_url)
        result = session_requests.get(drugs_url, headers=dict(referer=drugs_url))
        result.encoding = 'gbk'
        jdat = json.loads(result.text)
        variantations = jdat['data']['variantAnnotations']
        clinical_annotations = jdat['data']['clinicalAnnotations']
        # print(type(variantations))
        # pa = 'PA448385'
        pa = drug
        # for clinical in clinical_annotations:
            # if num == 0:

        for variant in variantations:
            if num == 0:
                # print(type(variant))
                # print(variant.keys())
                indexs = ['genes', 'chemicals', 'pvalue', 'literature', 'significance', 'phenotypeCategories',
                          'variants', 'cases', 'notes', 'characteristics', 'race', 'sentence', 'literatureUrl', 'id']
                # print(indexs)
                dfi.write('PA_ID\t'+'\t'.join(indexs)+'\n')
            num += 1
            line = pa
            for key in indexs:
                if key not in variant.keys():
                    line += '\tnull'
                    continue
                    # print(key, type(variant[key]))
                if isinstance(variant[key], int):
                    line += '\t{}'.format(variant[key])
                if isinstance(variant[key], str):
                    variant[key] = variant[key].replace('\n', '')
                    line += '\t{}'.format(variant[key])
                if isinstance(variant[key], list):
                    line += '\t'
                    for tp in variant[key]:
                        if isinstance(tp, dict):
                            line += '{},'.format(tp['text'])
                        elif isinstance(tp, str):
                            line += '{},'.format(tp)
                        else:
                            print(tp)
            dfi.write('{0}\n'.format(line))
    dfi.close()


if __name__ == '__main__':
    st = time.time()
    scrap_data()
    print('use time: {}'.format(time.time()-st))
