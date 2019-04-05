
python -m celery worker -n adder --concurrency=1 --loglevel=INFO --app=adder:app -Q adder_queue
