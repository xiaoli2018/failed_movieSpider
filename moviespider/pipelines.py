# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys

reload(sys)

sys.setdefaultencoding('utf8')

class MoviespiderPipeline(object):
    def process_item(self, item, spider):
        text = 'movie.txt'
        content = '迅雷链接  %s' % item['link']
        with open(text,'wb') as handles:
            handles.write(content)
        return item
