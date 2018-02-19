#! /bin/bash

cd /worker && python3 -m celery worker --concurrency=$WORKER_PROCESSES --loglevel=INFO --app=$WORKER_NAME:app -Q $WORKER_Q
