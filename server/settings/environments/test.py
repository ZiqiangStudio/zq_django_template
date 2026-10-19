from server.settings import ZQ_EXCEPTION

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

SECRET_KEY = "test-secret-key-for-running-automated-tests"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"

ZQ_EXCEPTION["EXCEPTION_UNKNOWN_HANDLE"] = False

DRF_LOGGER = {
    "DEFAULT_DATABASE": "default",
    "QUEUE_MAX_SIZE": 50,
    "INTERVAL": 10,
}
