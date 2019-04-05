
from config import Config as conf
from workflow import get_celery_app, VectorMultiplicationWorkFlow, SingleNeroNetLayerWorkFlow, LongChainAdd, SingleNeroNetLayerWithLongAddWorkFlow

app = get_celery_app(broker_url=conf.CELERY_BROKER_URL, result_backend=conf.CELERY_RESULT_BACKEND)

def main():
    # vmwf = VectorMultiplicationWorkFlow(app)
    vmwf = SingleNeroNetLayerWorkFlow(app)
    results = []
    for i in range(10):
        result = vmwf.execute([i, i+1], [i+3, i+4])
        results.append(result)
    print(results)
    return results

if __name__ == "__main__":
    results = main()
    # nnlayer = SingleNeroNetLayerWorkFlow(app)
    # result = nnlayer.execute([.1, .2], [.4, .5])
    # vmwf = VectorMultiplicationWorkFlow(app)
    # vres = vmwf.execute([.1, .2], [.4, .5])
    # longadd = SingleNeroNetLayerWithLongAddWorkFlow(app)
    # added = longadd.execute([.1, .2], [.4, .5])
