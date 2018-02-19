

from abc import ABCMeta
from os import getenv
from celery.result import ResultBase
from logging import getLogger
from time import sleep
from celery import Celery, chain, task, signature, group, chord


logger = getLogger(name="proclog")
# logger.setlevel('INFO')

from config import Config as conf
from celery import chain

def get_celery_app(broker_url, result_backend):
    app = Celery()
    app.conf.update(
        BROKER_URL=broker_url,
        CELERY_RESULT_BACKEND=result_backend,
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
        CELERY_ACCEPT_CONTENT=['json'],
        CELERY_IGNORE_RESULT=False,
        CELERY_RESULT_PERSISTENT=False,
        CELERY_TIMEZONE='Europe/London',
        CELERY_ENABLE_UTC=True
    )
    CELERY_USE_SSL = getenv("BROKER_USE_SSL")
    BROKER_URL = getenv("BROKER_URI")
    if CELERY_USE_SSL:
        from ssl import CERT_REQUIRED, CERT_OPTIONAL, CERT_NONE
        ssl_conf = {'ssl_cert_reqs': CERT_NONE, 'ssl_ca_certs':None, 'ssl_certfile':None, 'ssl_keyfile':None}
        app.conf.update(
            CELERY_REDIS_BACKEND_USE_SSL=ssl_conf,
            REDIS_BROKER_USE_SSL=ssl_conf,
            BROKER_USE_SSL=ssl_conf,
            BACKEND_USE_SSL=ssl_conf,
            redis_backend_use_ssl=ssl_conf
        )
    return app


class Workflow(metaclass=ABCMeta):

    def __init__(self, app, config=None):
        self.app = app
        self.config = config

    def execute(self):
        raise NotImplementedError()


class VectorMultiplicationWorkFlow(Workflow):

    def execute(self, xs, ys):
        mul_sigs = [signature("multiper.worker.work", kwargs={'x':x, 'y':y}, app=self.app, queue="multiper_queue")
                    for x, y in zip (xs, ys)]
        mulgrp = group(*mul_sigs)
        sum_sigs = signature("adder.worker.work", app=self.app, queue="adder_queue")
        flow = chord(mulgrp)(sum_sigs)
        return flow

