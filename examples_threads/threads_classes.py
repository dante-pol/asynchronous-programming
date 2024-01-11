from threading import Thread
import time


class SomeThread(Thread):
    def __init__(self, id: int or str, delay: int):
        super().__init__()

        self.id = id
        self.delay = delay

    def run(self):
        print("Some code...\n")
        time.sleep(self.delay)
        print("Some code...")


def main():
    tr = SomeThread("Kar kar", 3)
    tr.start()

    input("input some data >>")


if __name__ == '__main__':
    main()
