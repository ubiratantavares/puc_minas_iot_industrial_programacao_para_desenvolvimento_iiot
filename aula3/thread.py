from threading import *

import time

def tarefa1():
    for i in range(6):
        print("Thread 1")
        time.sleep(1)

def main_1():
    t1 = Thread(target=tarefa1, daemon=True)
    t1.start()
    time.sleep(3)
    print("Main encerrado")

def main_2():
    t1 = Thread(target=tarefa1, daemon=False)
    t1.start()
    time.sleep(3)
    print("Main encerrado")

if __name__ == '__main__':
    #main_1()
    main_2()
    