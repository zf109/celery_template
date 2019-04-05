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


def make_chain(sigs, app=None):
    """
        takes the input of the form:
        [
            {
                "name": <signature_name>,
                "args": <signature_args>,
                "queue": <signature_queue>,
            },
            {
                "name": <signature_name>,
                "args": <signature_args>,
                "queue": <signature_queue>,
            },
        ]
    """
    signatures = []
    for sig_dict in sigs:
        sig_name = sig_dict["name"]
        sig_args = sig_dict["args"] if "args" in sig_dict.keys() else None
        sig_kwargs = sig_dict["kwargs"] if "kwargs" in sig_dict.keys() else None
        sig_queue = sig_dict["queue"] if "queue" in sig_dict.keys() else None
        sig = signature(sig_name, args=sig_args, kwargs=sig_kwargs, app=app, queue=sig_queue)
        signatures.append(sig)
    
    return chain(*signatures)


