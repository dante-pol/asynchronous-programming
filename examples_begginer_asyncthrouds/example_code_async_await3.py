import asyncio

async def task1():
    print("Run task1")
    await asyncio.sleep(5)
    print("Completed task1")
    return 3

async def task2(delay: int or float):
    print("Run task2")
    await asyncio.sleep(delay)
    print("Completed task2")


async def task3():
    print("Run task3")
    await asyncio.sleep(7)
    print("Completed task3")

def func():
    print("Stopped coroutine...")

async def main():
    t1 = asyncio.create_task(task1())
    await t1

    if not t1.done():
        await asyncio.create_task(task2(t1.result()))
    else:
        await asyncio.create_task(task3())


if __name__ == "__main__":
    print("Starting program...")
    asyncio.run(main())
    print("Completed program...")