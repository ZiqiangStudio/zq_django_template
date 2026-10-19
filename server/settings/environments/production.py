from django.core.exceptions import ImproperlyConfigured
from server.settings.util import Csv, config
from server.settings.components.configs import CacheConfig

# debug 模式
DEBUG = config("DJANGO_DEBUG", False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=Csv())

SERVER_URL = config("SERVER_URL", default="")

# 生产环境强校验 Fail Fast
if not config("DATABASE_URL", default=""):
    raise ImproperlyConfigured("CRITICAL: DATABASE_URL must be configured in production environment.")

secret_key = config("DJANGO_SECRET_KEY", default="")
if not secret_key or "insecure" in secret_key:
    raise ImproperlyConfigured("CRITICAL: A secure DJANGO_SECRET_KEY must be configured in production environment.")

# region Cache
CACHES = CacheConfig.get()
# endregion
