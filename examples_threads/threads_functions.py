import _thread
import time


def solver_first(delay: int or float):
    count = 0
    while count < 5:
        time.sleep(delay)
        print("Solver 1")
        count += 1


def solver_second(delay: int or float):
    count = 0
    while count < 3:
        print("Solver 2")
        count += 1
        time.sleep(delay)

def main():
    _thread.start_new_thread(solver_first, (1, ))
    _thread.start_new_thread(solver_second, (0.5, ))
    time.sleep(1)

    print("Kara for Asad!")

main()