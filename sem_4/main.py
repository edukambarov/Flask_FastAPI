import argparse
from pathlib import Path
import threading, asyncio, multiprocessing
import os, time
import requests

fin_async = 0.0
fin_threading = 0.0
fin_multiprocessing = 0.0

data_images = []
with open('images.txt','r',encoding='utf-8') as images:
    for img in images.readlines():
        data_images.append(img.strip())

image_path = Path('./images/')


def download_img(url):
    start_time = time.time()
    response = requests.get(url, stream=True)
    filename = image_path.joinpath(os.path.basename(url))
    with open(filename, 'wb', encoding='utf-8') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    end_time = time.time() - start_time
    print(f'Загрузка {filename} завершена за {end_time:.2f} секунд')


async def download_img_async(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_img(url))
        tasks.append(task)

    await asyncio.gather(*tasks)
    end_time = time.time() - start_time
    print(f'Загрузка завершена за {end_time:.2f} секунд')

def download_img_multiprocessing(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=download_img, args=(url,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    end_time = time.time() - start_time
    print(f'Загрузка завершена за {end_time:.2f} секунд')

def download_img_threading(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download_img, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end_time = time.time() - start_time
    print(f'Загрузка завершена за {end_time:.2f} секунд')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа-парсер для добавления изображеий по URL-адресам')
    parser.add_argument(default=data_images,
                        nargs="+",
                        help='Список URL-адресов источников изображений')
    args = parser.parse_args()

    urls = args.urls
    if not urls:
        urls = data_images

    print(f'Загрузка {len(urls)} изображений многопоточным методом')
    download_img_threading(urls)

    print(f'Загрузка {len(urls)} изображений многопроцессорным методом')
    download_img_multiprocessing(urls)

    print(f'Загрузка {len(urls)} изображений асинхронным методом')
    asyncio.run(download_img_async(urls))