import asyncio


async def task1():
    print("Run task1")
    await asyncio.sleep(5)
    print("Completed task1")


async def task2():
    print("Run task2")
    await asyncio.sleep(6)
    print("Completed task2")


async def task3():
    print("Run task3")
    await asyncio.sleep(7)
    print("Completed task3")


async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    t3 = asyncio.create_task(task3())

    await t1
    await t2
    await t3


if __name__ == "__main__":
    asyncio.run(main())
