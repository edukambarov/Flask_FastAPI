# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте процессы.
import os
import multiprocessing
import time
from pathlib import Path

import requests

urls = [
'https://www.sports.ru/football/1116105812-red-bull-stanet-titulnym-sponsorom-lidsa-v-sleduyushhem-sezone-kompani.html',
'https://www.sports.ru/football/1116105743-direktor-bavarii-o-kompani-odin-iz-samyx-interesnyx-trenerov-v-evrope-.html',
'https://www.sports.ru/hockey/1116105793-ovechkin-o-razvyazke-rpl-bylo-obidno-za-dinamo-i-za-bolelshhikov-vse-b.html'
    ]

file_dir = Path(Path.cwd(), 'downloaded')

def count_words(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        print(f'Файл {file_path} содержит {len(f.read().split())} слов')

if __name__ == '__main__':
    processes = []
    for file in os.listdir(file_dir):
        if Path(file_dir, file).is_file():
            process = multiprocessing.Process(target=count_words, args=(Path(file_dir, file),))
            processes.append(process)
            process.start()

    for p in processes:
        p.join()

