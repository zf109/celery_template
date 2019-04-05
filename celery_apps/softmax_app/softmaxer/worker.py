import numpy as np
from time import sleep
from random import random
from .celery_app import get_celery_app
from .config import Config as conf

app = get_celery_app(broker_url=conf.CELERY_BROKER_URL, result_backend=conf.CELERY_RESULT_BACKEND)

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

@app.task
def work(x):
    sleep(2 + random())
    return softmax(x)
