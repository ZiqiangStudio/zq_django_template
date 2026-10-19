from django.db import models


class FileType(models.IntegerChoices):
    """
    文件类型状态
    """

    UNKNOWN = 0, "未知"
    RESUME = 1, "简历"
    WORK = 2, "作品"
    MANAGER = 3, "管理员"
