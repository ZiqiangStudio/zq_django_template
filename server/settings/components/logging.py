# Logging
# https://docs.djangoproject.com/en/3.2/topics/logging/
import sys

from loguru import logger

from server.settings.components.configs import LogConfig
from server.settings.util import config

# See also:
# 'Do not log' by Nikita Sobolev (@sobolevn)
# https://sobolevn.me/2020/03/do-not-log


# region DRF_LOGGER
DRF_LOGGER = {
    "DATABASE": True,
    "METHODS": config(
        "DRF_API_LOGGER_METHODS",
        "POST, PUT, PATCH, DELETE",
        cast=lambda v: [s.strip() for s in v.split(",")],
    ),
    "SKIP_URL_NAME": ["test-list", "base-test-list"],  # 忽略测试 api 的日志
    "SENSITIVE_KEYS": ["password"],  # 需要隐藏的字段
}
# endregion

# 適配loguru
LOGGING = LogConfig.get_config()

logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "level": config("LOG_LEVEL", "INFO"),
            "format": (
                "<blue>{time:HH:mm:ss.SSS}</blue> | "
                "<level>{level: <8}</level> | "
                "<level>{message}</level> - "
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
            ),
        }
    ],
)
