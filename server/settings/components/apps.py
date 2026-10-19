DJANGO_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS: list[str] = [
    "rest_framework",  # DRF
    "corsheaders",  # CORS 跨域
    "rest_framework_simplejwt",  # JWT
    "drf_spectacular",  # OpenAPI / Swagger 文档
    "django_filters",  # 过滤器
    "drf_standardized_errors",  # DRF 错误处理
    "zq_django_util.logs",  # 日志记录
]

LOCAL_APPS: list[str] = [
    "users",  # 用户
    "oauth",  # 认证与登录
]

INSTALLED_APPS: list[str] = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE: list[str] = [
    "corsheaders.middleware.CorsMiddleware",  # CORS 跨域(最外层)
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "zq_django_util.logs.middleware.APILoggerMiddleware",  # 请求日志
]

ROOT_URLCONF = "server.urls"

WSGI_APPLICATION = "server.wsgi.application"
ASGI_APPLICATION = "server.asgi.application"
