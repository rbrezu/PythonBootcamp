from multiprocessing import Pool
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print ('Elapsed time: {}'.format(end-start))
        return result
    return wrapper

n = 10 ** 8
procs = 8


def sum_nums(args):
    low = int(args[0])
    high = int(args[1])
    return sum(range(low, high + 1))

@timing
def normal():
    return sum(range(1, n + 1))

@timing
def mprocs():
    sizeSegment = n / procs

    # Create size segments list
    jobs = []
    for i in range(0, procs):
        jobs.append((i * sizeSegment + 1, (i + 1) * sizeSegment))

    pool = Pool(procs).map(sum_nums, jobs)
    result = sum(pool)

    return result

@timing
def mthreads():
    sizeSegment = n / procs

    # Create size segments list
    jobs = []
    for i in range(0, procs):
        jobs.append((i * sizeSegment + 1, (i + 1) * sizeSegment))

    pool = ThreadPoolExecutor(max_workers=procs).map(sum_nums, jobs)
    result = sum(pool)

    return result


if __name__ == "__main__":
    print ('Normal {}: '.format(normal()))
    print ('Threding {}: '.format(mthreads()))
    print ('Proccesing {}: '.format(mprocs()))
