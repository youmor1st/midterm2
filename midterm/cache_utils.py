from django.core.cache import cache
import logging

cache_logger = logging.getLogger('cache')

def cache_get_with_logging(key):
    result = cache.get(key)
    if result:
        cache_logger.debug(f"Cache hit for key: {key}")
    else:
        cache_logger.debug(f"Cache miss for key: {key}")
    return result

def cache_set_with_logging(key, value, timeout):
    cache.set(key, value, timeout)
    cache_logger.debug(f"Cache set for key: {key}")
