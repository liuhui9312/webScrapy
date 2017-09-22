#!/usr/bin/python
# -*- coding: utf-8 -*-

from gkb_spider.Mysql import Sql
from gkb_spider.items import GkbSpiderItem


class GkbSpiderPipeline(object):

    def process_item(self, item, spider):
        #deferToThread(self._process_item, item, spider)
        if isinstance(item, GkbSpiderItem):
            if item['num'] != 'null':
                for i in range(int(item['num'])):
                    ret = Sql.select_name(items=item, num=i)
                    # print('check exists state {} '.format(ret))
                    if ret == 1:
                        # print(item['pa_id'] + '已经存在了')
                        pass
                    else:
                        Sql.insert_pharmgkb(items=item, num=i)
                        # print('开始存药物{}'.format(item['pa_id']))
            else:
                # print('{} can not find any annotation!'.format(item['pa_id']))
                pass
        else:
            pass

