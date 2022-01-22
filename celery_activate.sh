#!/usr/bin/bash

source ./venv/bin/activate

cd ./django_test
celery -A  celery_test_proj worker --loglevel=info
