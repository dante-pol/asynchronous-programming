import random
import time
from threading import Thread
from tkinter import *

COUNTER_THREADS = 0


class LoaderThread(Thread):

    def __init__(self, id: int or str):
        Thread.__init__(self)

        self.id = id

    def run(self):
        for i in range(1, 100):
            print(f"{i}% loading...")
            time.sleep(random.randint(1, 10) / 10)

        print(f"{self.name} thread is completed...")


class Window(Frame):

    def __init__(self, root, loader):
        super().__init__(root)

        self.loader = loader

        self.pack()
        self.build()

    def build(self):
        self.__build_buttons()

    def __build_buttons(self):
        for i in range(0, 5, 1):
            btn = Button(self, text=f"Name_{i}", command=self.loader)
            btn.config(width=25, height=2)
            btn.grid(row=i, column=i)


def main():
    app = Tk("App Example")
    app.geometry("950x225")

    window = Window(app, loader)

    app.mainloop()


def loader():
    global COUNTER_THREADS

    COUNTER_THREADS += 1

    th = LoaderThread(COUNTER_THREADS)
    th.start()


if __name__ == "__main__":
    main()