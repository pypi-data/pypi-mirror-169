from scrapy_redis.defaults import *


SCHEDULER_DUPEFILTER_KEY = '%(spider)s:cuckoofilter'
DUPEFILTER_DEBUG = False


CUCKOOFILTER_BUCKETSIZE = 2    # 布谷鸟过滤器桶的大小
CUCKOOFILTER_CAPACITY_BIT = 18 # 去重数量 2 ** 18
CUCKOOFILLTER_EXPANSION = 2    # 允许自动扩展空间的次数
