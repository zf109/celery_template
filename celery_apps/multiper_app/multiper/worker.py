
from time import sleep
from random import random
from .celery_app import get_celery_app
from .config import Config as conf

app = get_celery_app(broker_url=conf.CELERY_BROKER_URL, result_backend=conf.CELERY_RESULT_BACKEND)

@app.task
def work(x, y):
    sleep(5 + 2 * random())
    return x * y
