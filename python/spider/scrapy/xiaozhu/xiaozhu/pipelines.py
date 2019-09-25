# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class XiaozhuPipeline(object):
    def process_item(self, item, spider):
        fp = open('Z:/git/Git/git/learngit/python/spider/scrapy/xiaozhu.txt','a+')
        fp.write(item['title']+'\n')
        fp.close()
        return item
