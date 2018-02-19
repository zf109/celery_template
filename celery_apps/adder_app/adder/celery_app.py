
from logging import getLogger
from logging import INFO
from celery import Celery
from os import getenv

_logger = getLogger('transcription_worker')
_logger.setLevel(INFO)

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
