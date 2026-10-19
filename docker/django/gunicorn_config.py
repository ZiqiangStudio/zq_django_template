# Gunicorn configuration file
# https://docs.gunicorn.org/en/stable/configure.html#configuration-file
# https://docs.gunicorn.org/en/stable/settings.html

import multiprocessing
import os

bind = "0.0.0.0:8000"
# Concerning `workers` setting see:
# https://github.com/wemake-services/wemake-django-template/issues/1022
workers = os.environ.get(
    "GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1
)

max_requests = 2000
max_requests_jitter = 400

log_file = "-"
chdir = "/app"
worker_tmp_dir = "/dev/shm"  # noqa: S108
