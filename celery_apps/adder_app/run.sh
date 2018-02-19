
python -m celery worker --concurrency=2 --loglevel=INFO --app=adder:app -Q adder_queue
