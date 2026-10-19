from server import __version__ as server_version

# region DRF
REST_FRAMEWORK = {
    # 异常处理
    "EXCEPTION_HANDLER": "zq_django_util.exceptions.handler.exception_handler",
    # 认证配置
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    # 全局认证 优先级高于试图类中的配置 login view 中，进行用户验证时
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "zq_django_util.utils.auth.authentications.ActiveUserAuthentication",
    ],
    # 自定义渲染器
    "DEFAULT_RENDERER_CLASSES": [
        "zq_django_util.response.renderers.CustomRenderer",
    ],
    # api 默认文档
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # 过滤器
    "DEFAULT_FILTER_BACKENDS": (
        "rest_framework.filters.OrderingFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
    # 分页
    "DEFAULT_PAGINATION_CLASS": "zq_django_util.utils.pagination.GlobalPageNumberPagination",
}

# DRF扩展
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    "DEFAULT_CACHE_RESPONSE_TIMEOUT": 60 * 30,
    # 缓存存储
    "DEFAULT_USE_CACHE": "view",
}
# endregion

# DRF文档
SPECTACULAR_SETTINGS = {
    "TITLE": "自强 Studio 后端 API 文档",
    "DESCRIPTION": "Ziqiang Studio Backend API Documentation",
    "VERSION": server_version,
}
# endregion
