
from celery import group
from config import Config as conf
from process import async_mulvec



def main():
    print(async_mulvec([1, 2, 3],[4, 5, 6]))

if __name__ == "__main__":
    main()

