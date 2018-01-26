
from celery import group
from celery.result import ResultBase
from logging import getLogger
from time import sleep

logger = getLogger(name="proclog")
# logger.setlevel('INFO')

from celery_app.celery_app import get_celery_app
from config import Config as conf

app = get_celery_app(broker_url=conf.CELERY_BROKER_URL, result_backend=conf.CELERY_RESULT_BACKEND)

# @app.task(name="add")
# def add(x, y):
#     return x + y

@app.task(name="mul", trail=True)
def mul(x, y):
    sleep(5)
    return x * y

@app.task(name="mul10", trail=True)
def mul10(x, y):
    sleep(10)
    return x * y

@app.task(name="async_mulvec")
def async_mulvec(xs, ys):
    result = group(mul.s(x, y) for x, y in zip(xs, ys))()
    return sum(result.get(timeout=20))
