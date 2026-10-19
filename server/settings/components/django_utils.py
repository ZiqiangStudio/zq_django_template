from server.settings.util import config

ZQ_EXCEPTION = {
    "EXCEPTION_UNKNOWN_HANDLE": not config("DEBUG", True, bool),
    "EXCEPTION_HANDLER_CLASS": "zq_django_util.exceptions.handler.ApiExceptionHandler",
}
