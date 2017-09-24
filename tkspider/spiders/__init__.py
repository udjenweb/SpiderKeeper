# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import logging
import os
import time
from tkspider.settings import BASE_DIR, LOG_ROOT


class BaseSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super(BaseSpider, self).__init__(*args, **kwargs)
        # logger = logging.getLogger('spider_{}'.format(self.name))
        logger = self.logger.logger
        logger.setLevel(logging.DEBUG)

        spider_log_path = os.path.join(
            BASE_DIR, LOG_ROOT,
            '{spider_name}__{time}.log'.format(
                spider_name=self.name, time=time.strftime("%Y-%m-%d_%H-%M-%S")))

        logger.addHandler(logging.FileHandler(spider_log_path))


