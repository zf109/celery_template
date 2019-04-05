
from os import getenv

class Config(object):
    CELERY_BROKER_URL = getenv("BROKER_URI", "redis://localhost:6379")
    CELERY_RESULT_BACKEND = getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379")
