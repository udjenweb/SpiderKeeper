# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
from tkspider.settings import BASE_DIR, RESULTS_ROOT
import time

from scrapy import signals

class TkspiderPipeline(object):

    def __init__(self, crawler):
        self.crawler = crawler

    @classmethod
    def from_crawler(cls, crawler):
        this = cls(crawler)
        crawler.signals.connect(this.spider_opened, signals.spider_opened)
        crawler.signals.connect(this.spider_closed, signals.spider_closed)
        return this

    def spider_opened(self, spider):

        spider_results_path = os.path.join(
            BASE_DIR, RESULTS_ROOT,
            '{spider_name}__{time}.jl'.format(
                spider_name=spider.name,
                time=time.strftime("%Y-%m-%d_%H-%M-%S"))
        )
        self.file = open(spider_results_path, 'w')

    def spider_closed(self, spider):
        self.file.close()

        total_count_ads = getattr(spider, 'total_count_ads', -1)
        self.crawler.stats.set_value('total_count_ads', total_count_ads)

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item

