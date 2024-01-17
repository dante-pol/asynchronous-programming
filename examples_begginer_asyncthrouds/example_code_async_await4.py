import asyncio


async def task1():
    print("Run task1")
    await asyncio.sleep(5)
    print("Completed task1")
    return 3


async def task2():
    print("Run task2")
    await asyncio.sleep(1)
    print("Completed task2")


async def task3():
    print("Run task3")
    await asyncio.sleep(7)
    print("Completed task3")


async def main():
    await task1()
    await task2()
    await task3()


if __name__ == "__main__":
    print("Starting program...")
    asyncio.run(main())
    print("Completed program...")
