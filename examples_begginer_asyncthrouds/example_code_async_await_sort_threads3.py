import asyncio
import random as r


def bubble_sort(array: list, type=lambda x, y: x > y, key=lambda x: x):
    array_sorted = array.copy()
    length = len(array_sorted)
    for i in range(0, length - 1, 1):
        for j in range(0, length - 1 - i, 1):
            if type(array_sorted[j], array_sorted[j + 1]):
                array_sorted[j], array_sorted[j + 1] = array_sorted[j + 1], array_sorted[j]
    print("-"*20)
    print(array_sorted)


async def main():
    main_task = await asyncio.gather(
        asyncio.to_thread(bubble_sort, [r.randint(-10, 10) for i in range(r.randint(10, 1000))]),
        asyncio.to_thread(bubble_sort, [r.randint(-10, 10) for i in range(r.randint(10, 1000))]),
        asyncio.to_thread(bubble_sort, [r.randint(-10, 10) for i in range(r.randint(10, 1000))]),
    )

if __name__ == "__main__":
    asyncio.run(main())
