# Задание №7

# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

from random import randint
import threading, multiprocessing, asyncio
import time

main_lst = [randint(1,101) for _ in range(1_000_000)]
counter = 0

def increment(num_lst):
    global counter
    for num in num_lst:
        counter += num
    print(counter)



if __name__ == '__main__':
    # start_time = time.time()
    # threads = []
    # lsts_num = [main_lst[i:i+100_000] for i in range(10)]
    # for i in range(10):
    #     t = threading.Thread(target=increment, args=(lsts_num[i],))
    #     threads.append(t)
    #     t.start()
    #
    # for t in threads:
    #     t.join()
    #
    # print(f'All threads completed work. Time spent: {time.time() -start_time:0.02f} seconds.')

    start_time = time.time()
    processes = []
    lsts_num = [main_lst[i:i+100_000] for i in range(10)]
    for i in range(10):
        p = multiprocessing.Process(target=increment, args=(lsts_num[i],))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'All processes completed work. Time spent: {time.time() -start_time:0.02f} seconds.')