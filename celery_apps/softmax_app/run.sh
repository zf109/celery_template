
python -m celery worker -n softmaxer --concurrency=2 --loglevel=INFO --app=softmaxer:app -Q softmaxer_queue
