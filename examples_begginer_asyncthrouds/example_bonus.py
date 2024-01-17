import asyncio
import aiohttp
import os

async def download_file(session, url, destination):
    """ Асинхронная функция для загрузки файла по URL. """
    async with session.get(url) as response:
        with open(destination, 'w') as file:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                file.write(chunk)
        print(f'Файл загружен: {destination}')

async def main(urls):
    """ Запускает загрузку файлов. """
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url, f"file_{index}.txt") for index, url in enumerate(urls)]
        await asyncio.gather(*tasks)

# Список URL файлов для загрузки
urls = [
    'https://example.com/data1.txt',
    'https://example.com/data2.txt',
    ...
]

# Запуск асинхронного загрузчика файлов
asyncio.run(main(urls))
