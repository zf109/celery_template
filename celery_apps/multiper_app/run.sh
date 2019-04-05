
python -m celery worker -n multiper --concurrency=6 --loglevel=INFO --app=multiper:app -Q multiper_queue
