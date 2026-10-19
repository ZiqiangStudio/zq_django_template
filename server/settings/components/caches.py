from server.settings.components.configs import CacheConfig

CACHES = CacheConfig.get()

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"
