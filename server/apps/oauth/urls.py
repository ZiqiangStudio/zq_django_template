from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    PasswordLoginView,
    ZqAuthLoginView,
)

urlpatterns = [
    path(
        "login/zq/",
        ZqAuthLoginView.as_view(),
        name="zq_auth_login",
    ),  # 自强 CAS 统一认证登录
    path(
        "login/password/",
        PasswordLoginView.as_view(),
        name="password_login",
    ),  # 账号密码登录
    path(
        "login/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),  # 刷新 JWT Token
]
