# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
from tkspider.settings import BASE_DIR, RESULTS_ROOT
import time


class TkspiderPipeline(object):
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):

        spider_results_path = os.path.join(
            BASE_DIR, RESULTS_ROOT,
            '{spider_name}__{time}.jl'.format(
                spider_name=spider.name,
                time=time.strftime("%Y-%m-%d_%H-%M-%S"))
        )
        self.file = open(spider_results_path, 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item

