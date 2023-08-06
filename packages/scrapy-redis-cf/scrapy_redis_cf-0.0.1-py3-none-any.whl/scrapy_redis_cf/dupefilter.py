import logging
import time
import redis

from scrapy.dupefilters import BaseDupeFilter
from scrapy.exceptions import NotConfigured
from scrapy.utils.request import request_fingerprint
from .exception import RedisNoBloomException
from . import defaults


logger = logging.getLogger(__name__)


# TODO: Rename class to RedisDupeFilter.
class RFPDupeFilter(BaseDupeFilter):
    logger = logger

    def __init__(self, server, key, bucket_size, expansion, capacity, debug=False):
        """
        server: redis.Redis
        key: redis key
        bucket_size: 桶的大小
        expansion: 支持扩展的次数
        capacity: 容量
        """
        self.server = server
        self.key = key
        self.debug = debug
        self.bucket_size = bucket_size
        self.expansion = expansion
        self.capacity = capacity
        self.logdupes = True
        self.bf = server.cf()
        self.valid_redis_has_bloom()
        if not server.exists(key):
            self.bf.create(key, capacity, expansion=expansion, bucket_size=bucket_size)
        else:
            if server.type(key) != "MBbloomCF":
                server.delete(key)
                self.bf.create(key, capacity, expansion=expansion, bucket_size=bucket_size)

    def valid_redis_has_bloom(self):
        try:
            self.bf.info('a')
        except Exception as e:
            if "unknown command" in str(e):
                raise RedisNoBloomException

    @classmethod
    def from_settings(cls, settings):
        redis_url = settings.get("REDIS_URL")
        if not redis_url:
            logger.error("未配置REDIS_URL！")
            raise NotConfigured
        server = redis.StrictRedis.from_url(redis_url, decode_responses=True)
        key = defaults.DUPEFILTER_KEY % {'timestamp': int(time.time())}
        bucket_size = settings.get('CUCKOOFILTER_BUCKETSIZE', defaults.CUCKOOFILTER_BUCKETSIZE)
        capacity = settings.get('CUCKOOFILTER_CAPACITY_BIT', defaults.CUCKOOFILTER_CAPACITY_BIT)
        expansion = settings.getint('CUCKOOFILLTER_EXPANSION', defaults.CUCKOOFILLTER_EXPANSION)
        debug = settings.getbool('DUPEFILTER_DEBUG')
        return cls(server, key=key, bucket_size=bucket_size, expansion=expansion, capacity=capacity, debug=debug)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)
    
    @classmethod
    def from_spider(cls, spider):
        settings = spider.settings
        redis_url = settings.get("REDIS_URL")
        if not redis_url:
            logger.error("未配置REDIS_URL！")
            raise NotConfigured
        server = redis.StrictRedis.from_url(redis_url, decode_responses=True)
        key = defaults.SCHEDULER_DUPEFILTER_KEY % {'spider': spider.name}
        bucket_size = settings.get('CUCKOOFILTER_BUCKETSIZE', defaults.CUCKOOFILTER_BUCKETSIZE)
        capacity = settings.get('CUCKOOFILTER_CAPACITY_BIT', defaults.CUCKOOFILTER_CAPACITY_BIT)
        expansion = settings.getint('CUCKOOFILLTER_EXPANSION', defaults.CUCKOOFILLTER_EXPANSION)
        debug = settings.getbool('DUPEFILTER_DEBUG')
        return cls(server, key=key, bucket_size=bucket_size, expansion=expansion, capacity=capacity, debug=debug)

    def request_seen(self, request):
        """
        request : scrapy.http.Request
        """
        fp = self.request_fingerprint(request)
        added = self.bf.addnx(self.key, fp)
        return added == 0

    def request_fingerprint(self, request):
        return request_fingerprint(request)

    def close(self, reason=''):
        self.clear()

    def clear(self):
        """Clears fingerprints data."""
        self.server.delete(self.key)

    def log(self, request, spider):
        """Logs given request.

        Parameters
        ----------
        request : scrapy.http.Request
        spider : scrapy.spiders.Spider

        """
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        elif self.logdupes:
            msg = ("Filtered duplicate request %(request)s"
                   " - no more duplicates will be shown"
                   " (see DUPEFILTER_DEBUG to show all duplicates)")
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
            self.logdupes = False
        spider.crawler.stats.inc_value('cuckoofilter/filtered', spider=spider)
