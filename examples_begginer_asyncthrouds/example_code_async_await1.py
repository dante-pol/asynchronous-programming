import asyncio


async def task1():
    print("Run task1")
    await task2()
    print("Completed task1")

async def task2():
    print("Run task2")
    await task3()
    print("Completed task2")


async def task3():
    print("Run task3")
    await asyncio.sleep(3)
    print("Completed task3")

async def main():
    t = asyncio.create_task(task1())
    # t.add_done_callback(lambda : print("Stop coroutine..."))
    await asyncio.sleep(5)
    print("Stop main coroutine...")


if __name__ == "__main__":
    asyncio.run(main())