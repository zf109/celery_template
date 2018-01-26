docker build $1 -t celery_async_main -f ./docker/Dockerfile-main .
docker build $1 -t celery_async_worker -f ./docker/Dockerfile-worker .

