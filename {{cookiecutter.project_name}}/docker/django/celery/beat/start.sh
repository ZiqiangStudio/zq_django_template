#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate --noinput

exec celery -A server beat -l INFO