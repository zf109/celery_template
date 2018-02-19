
python -m celery worker --concurrency=6 --loglevel=INFO --app=multiper:app -Q multiper_queue
