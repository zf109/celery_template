
from celery.result import AsyncResult
from workflow import get_celery_app
import pydot
import os


def trace(task_id, app=None):
    if not app:
        app = get_celery_app()
    task = AsyncResult(task_id)


def render_dot(file_path, out_path=None):
    out_path_ = out_path if out_path else '.'
    (graph,) = pydot.graph_from_dot_file(file_path)
    graph.write_png(os.path.join(out_path_, 'flow.png'))

