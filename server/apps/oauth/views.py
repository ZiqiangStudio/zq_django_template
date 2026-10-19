from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from zq_django_util.exceptions import ApiException
from zq_django_util.response import ResponseType

from users.models import User
from .serializers import (
    PasswordLoginSerializer,
    ZqAuthLoginSerializer,
)


class PasswordLoginView(TokenObtainPairView):
    """
    密码登录视图
    """

    serializer_class = PasswordLoginSerializer


class ZqAuthLoginView(TokenObtainPairView):
    """
    自强 CAS 统一认证登录视图
    """

    queryset = User.objects.all()
    serializer_class = ZqAuthLoginSerializer

    def post(self, request, *args, **kwargs):
        """
        支持通过 zq_auth code 获取 JWT Token
        """
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise ApiException(
                ResponseType.ThirdLoginFailed,
                msg="自强账号登录失败",
                detail="生成 token 时 simple jwt 发生 TokenError",
                record=True,
            ) from e

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
