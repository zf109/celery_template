python3 -m celery worker -n master --concurrency=4 --loglevel=INFO --app=main:app
