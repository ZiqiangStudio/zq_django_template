import socket
from server.settings.components.apps import INSTALLED_APPS, MIDDLEWARE
from server.settings.util import config

# Setting the development status:
DEBUG = True
SERVER_URL = config("SERVER_URL", "http://127.0.0.1:8000")
ALLOWED_HOSTS = ["*"]

# Optional development tools (auto-enabled if installed)
try:
    import debug_toolbar  # noqa: F401

    INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405

    def _custom_show_toolbar(request):
        return DEBUG

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": "server.settings.environments.development._custom_show_toolbar",
    }
except ImportError:
    pass

try:
    import nplusone.ext.django  # noqa: F401

    INSTALLED_APPS += ["nplusone.ext.django"]  # noqa: F405
    MIDDLEWARE += ["nplusone.ext.django.NPlusOneMiddleware"]  # noqa: F405
except ImportError:
    pass

try:
    import querycount  # noqa: F401

    MIDDLEWARE += ["querycount.middleware.QueryCountMiddleware"]  # noqa: F405
    QUERYCOUNT = {
        "THRESHOLDS": {
            "MEDIUM": 50,
            "HIGH": 200,
            "MIN_TIME_TO_LOG": 0,
            "MIN_QUERY_COUNT_TO_LOG": 0,
        },
        "IGNORE_REQUEST_PATTERNS": [
            r"^/admin/.*",
            r"^/static/.*",
            r"^/media/.*",
            r"^/docs/.*",
        ],
    }
except ImportError:
    pass

# Internal IPs for debug toolbar
try:
    INTERNAL_IPS = [
        f"{ip[: ip.rfind('.')]}.1"
        for ip in socket.gethostbyname_ex(socket.gethostname())[2]
    ]
except OSError:
    INTERNAL_IPS = []
INTERNAL_IPS += ["127.0.0.1"]
