from users.models import User
from zq_django_util.utils.auth.backends import OpenIdBackend


class UnionIdBackend(OpenIdBackend):
    """
    UnionID 验证模块(获取token时调用)
    """

    AuthUser = User  # 用户模型
    openid_field: str = "union_id"  # 获取字段名

    def __init__(self, auth_user_model=None):
        super().__init__(auth_user_model)
