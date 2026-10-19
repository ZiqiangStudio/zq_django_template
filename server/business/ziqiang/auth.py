from datetime import datetime
from uuid import UUID

from users.models import User
from zq_auth_sdk import (
    ThirdLoginFailedException,
    UserNotFoundException,
    ZqAuthClientException,
)
from zq_django_util.exceptions import ApiException
from zq_django_util.response import ResponseType

from server.business.ziqiang import zq_client


def get_union_id(code: str) -> UUID:
    """
    获取 union_id

    :param code: 临时 code

    :return: union_id

    :raise ApiException: 登录失败
    """
    try:
        union_id = zq_client.app.sso(code)["union_id"]
        return UUID(union_id)
    except ThirdLoginFailedException:
        raise ApiException(ResponseType.ThirdLoginFailed, msg="登录失败，请重试")
    except ZqAuthClientException as e:
        raise ApiException(ResponseType.ThirdServiceError, inner=e)


def fetch_user_info(user: User | UUID) -> dict:
    """
    获取用户信息

    :param user: 用户

    :return: 用户信息

    :raise ApiException: 获取用户信息失败
    :raise UserNotFoundException: 用户不存在
    """
    try:
        if isinstance(user, User):
            user = user.union_id

        data = zq_client.app.user_info(user, True)

        return {
            "name": data["name"],
            "User_id": data["User_id"],
            "phone": data["phone"],
            "update_time": datetime.fromisoformat(data["update_time"]),
        }
    except UserNotFoundException as e:
        raise e
    except ZqAuthClientException as e:
        raise ApiException(ResponseType.ThirdServiceError, inner=e)


def get_user_info_update_time(user: User) -> datetime:
    """
    获取用户信息更新时间

    :param user: 用户

    :return: 用户信息更新时间

    :raise ApiException: 获取用户信息失败
    :raise UserNotFoundException: 用户不存在
    """
    try:
        data = zq_client.app.user_info(user.union_id, True)

        return datetime.fromisoformat(data["update_time"])
    except UserNotFoundException as e:
        raise e
    except ZqAuthClientException as e:
        raise ApiException(ResponseType.ThirdServiceError, inner=e)
