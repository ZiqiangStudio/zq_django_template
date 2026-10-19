from datetime import datetime
from typing import Any
from uuid import UUID

from rest_framework_simplejwt.serializers import PasswordField
from zq_django_util.utils.auth.serializers import (
    OpenIdLoginSerializer as DefaultOpenIdLoginSerializer,
)

from oauth.backends import UnionIdBackend
from server.business.ziqiang.auth import get_union_id
from users.models import User


class ZqAuthLoginSerializer(DefaultOpenIdLoginSerializer):
    """
    自强 CAS 统一认证登录序列化器
    """

    backend = UnionIdBackend(User)
    openid = None
    openid_field = "union_id"
    code = PasswordField(label="前端获取code")  # 前端传入 code

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_token(cls, user: User):
        """
        自定义 JWT payload
        """
        token = super().get_token(user)
        token["is_staff"] = user.is_staff
        return token

    def generate_token_result(
        self,
        user: User,
        user_id_field: str,
        expire_time: datetime,
        access: str,
        refresh: str,
    ) -> dict:
        """
        生成登录接口返回结果
        """
        return {
            "id": getattr(user, user_id_field),
            "username": user.username,
            "is_active": user.is_active,
            "expire_time": expire_time,
            "access": access,
            "refresh": refresh,
        }

    def get_open_id(self, attrs: dict[str, Any]) -> UUID:
        """
        通过前端 code 获取自强 union_id
        """
        return get_union_id(attrs["code"])

    def handle_new_openid(self, union_id: UUID) -> User:
        """
        处理新用户注册与绑定
        """
        return super().handle_new_openid(union_id)


class PasswordLoginSerializer(DefaultOpenIdLoginSerializer):
    """
    账号密码登录序列化器
    """

    def generate_token_result(
        self,
        user: User,
        user_id_field: str,
        expire_time: datetime,
        access: str,
        refresh: str,
    ) -> dict:
        return {
            "id": getattr(user, user_id_field),
            "username": user.username,
            "is_active": user.is_active,
            "expire_time": expire_time,
            "access": access,
            "refresh": refresh,
            "is_superuser": user.is_superuser,
        }

    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token["is_staff"] = user.is_staff
        return token
