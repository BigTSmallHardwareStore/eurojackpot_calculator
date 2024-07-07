import multiprocessing as mp
from math import ceil
from time import time
from datetime import timedelta
from calculate_wins import *


def mp_worker(func, arg_list):
    for i in arg_list:
        func(i)


def main_multiprocessing(func, arg_list):
    s = time()
    cpu = mp.cpu_count()
    chunk_size = ceil(len(arg_list) / cpu)

    processes = []

    for i in range(cpu):
        p = mp.Process(target=mp_worker, args=(func, arg_list[chunk_size * i:chunk_size * (i + 1)],))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    e = time()
    print(timedelta(seconds=e - s))


if __name__ == '__main__':
    input_dir = 'all_possibilities'
    file_list = [filename for filename in os.listdir(input_dir)]

    main_multiprocessing(calculate_wins, file_list)
