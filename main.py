
from config import Config as conf
from workflow import get_celery_app, VectorMultiplicationWorkFlow

app = get_celery_app(broker_url=conf.CELERY_BROKER_URL, result_backend=conf.CELERY_RESULT_BACKEND)

def main():
    # async_mulvec_sig = signature("process.async_mulvec", args=([1, 2, 3],[4, 5, 6]), app=app)
    # app.send_task("process.async_mulvec", args=([1, 2, 3],[4, 5, 6]))
    # c = chain(async_mulvec_sig)
    # c()
    # app.send_task(async_mulvec)
    # print(async_mulvec([1, 2, 3],[4, 5, 6]))
    vmwf = VectorMultiplicationWorkFlow(app)
    results = []
    for i in range(10):
        result = vmwf.execute([i, i+1, i+2], [i+3, i+4, i+5])
        results.append(result)
    print(results)
    return results

if __name__ == "__main__":
    results = main()
