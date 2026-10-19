from server.settings.util import BASE_DIR, config

# region Static files
STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR.joinpath("static"))
# endregion

# region 媒体文件
MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR.joinpath("media"))
# endregion

# region OSS 与文件存储
# 本地开发默认使用本地文件系统；配置了 OSS 环境变量时切换到阿里云 OSS
if config("ALIYUN_OSS_ACCESS_KEY_ID", default="") and config("ALIYUN_OSS_ACCESS_KEY_SECRET", default=""):
    ALIYUN_OSS = {
        "ACCESS_KEY_ID": config("ALIYUN_OSS_ACCESS_KEY_ID"),
        "ACCESS_KEY_SECRET": config("ALIYUN_OSS_ACCESS_KEY_SECRET"),
        "ENDPOINT": config("ALIYUN_OSS_ENDPOINT", default="https://oss-cn-hangzhou.aliyuncs.com"),
        "BUCKET_NAME": config("ALIYUN_OSS_BUCKET_NAME", default=""),
        "URL_EXPIRE_SECOND": 60 * 60 * 24 * 30,
        "TOKEN_EXPIRE_SECOND": 60,
        "MAX_SIZE_MB": 100,
    }

    DEFAULT_FILE_STORAGE = "zq_django_util.utils.oss.backends.OssMediaStorage"
else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
# endregion
