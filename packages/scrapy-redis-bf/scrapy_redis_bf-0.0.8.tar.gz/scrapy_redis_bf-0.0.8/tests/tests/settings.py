# -*- coding: utf-8 -*-
BOT_NAME = 'tests'

SPIDER_MODULES = ['tests.spiders']
NEWSPIDER_MODULE = 'tests.spiders'

ROBOTSTXT_OBEY = False

SCHEDULER = "scrapy_redis_bf.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis_bf.dupefilter.RFPDupeFilter"

REDIS_URL = 'redis://:1751822472@r5.ikanade.cn:8379/0'

SCHEDULER_PERSIST = True
