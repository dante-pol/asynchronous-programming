import asyncio
import random as r


async def bubble_sort(array: list, type=lambda x, y: x > y, key=lambda x: x):
    array_sorted = array.copy()
    length = len(array_sorted)
    for i in range(0, length - 1, 1):
        for j in range(0, length - 1 - i, 1):
            if type(array_sorted[j], array_sorted[j + 1]):
                array_sorted[j], array_sorted[j + 1] = array_sorted[j + 1], array_sorted[j]
                await asyncio.sleep(1 / 1000)
    print(array_sorted)


async def main():
    # Schedule three calls *concurrently*:
    main_task = await asyncio.gather(
        bubble_sort([r.randint(-10, 10) for i in range(r.randint(10, 150))]),
        bubble_sort([r.randint(-10, 10) for i in range(r.randint(10, 150))]),
        bubble_sort([r.randint(-10, 10) for i in range(r.randint(10, 150))])
    )


def thread_run():
    print("Starting program...")
    asyncio.run(main())
    print("Completed program...")


if __name__ == "__main__":
    import _thread
    import time

    _thread.start_new_thread(thread_run, ())

    time.sleep(1)
    number = int(input("input >>"))
    if number == 0:
        print(number)
    else:
        print(-1)

    input()
