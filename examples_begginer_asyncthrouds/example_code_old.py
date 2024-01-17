import asyncio

@asyncio.coroutine
def task1():
    print("Run task1")

@asyncio.coroutine
def task2():
    print("Run task2")

@asyncio.coroutine
def task3():
    print("Run task3")


@asyncio.coroutine
def main():
    asyncio.create_task(task1)
    asyncio.create_task(task2)
    asyncio.create_task(task3)
