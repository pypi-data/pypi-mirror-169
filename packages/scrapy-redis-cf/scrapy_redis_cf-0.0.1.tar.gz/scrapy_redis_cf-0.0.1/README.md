# Scrapy-Redis-CuckooFilter

这是个scrapy_redis的布谷鸟过滤器版本，项目和 https://github.com/kanadeblisst/scrapy_redis_bf 基本一样

## 必要条件

需要redis加载了布隆过滤器的插件，默认安装的redis是没有加载的
具体请看：https://redis.io/docs/stack/bloom/quick_start/


## 安装

使用pip: `pip install scrapy-redis-cf`

## 使用

在scrapy项目里的 `settings.py`添加如下设置:

```python
SCHEDULER = "scrapy_redis_cf.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis_cf.dupefilter.RFPDupeFilter"

# 格式：redis://[:password@]host[:port][/database][?[timeout=timeout[d|h|m|s|ms|us|ns]][&database=database]]
REDIS_URL = 'redis://localhost:6379'
# 桶的大小，桶越大错误率越高, 但过滤器填充率越高
# 等于1时错误率最小为0.78%，等于3时为2.35%, 等于2时官网没说我也不知道
# https://redis.io/commands/cf.reserve/
CUCKOOFILTER_BUCKETSIZE = 2
# 去重数量 2 ** 18 , 
# 注意：实际容量要小于这个，因为布谷鸟过滤器很难完全填满
CUCKOOFILTER_CAPACITY_BIT = 18 
# 支持扩展容量的次数, 扩展次数越多，错误率越高
CUCKOOFILLTER_EXPANSION = 2

```

## 测试

下载该项目，然后运行里面的test spider即可

## Github

https://github.com/kanadeblisst/scrapy_redis_cf

