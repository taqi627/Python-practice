from threading import *

def show():
    print("Showed")

#t=Thread(target=show())
#t.start()

#print("Taskeen")

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("This is is a thread")

#t=MyThread()
#t.start()
#for i in range(5):
   # print("This is a main thread")


import time

class demo:
    def num(self):
        for i in range(1,6):
            print("The number is : ",i)
            time.sleep(2)

    def double(self):
        for i in range(1,6):
            print("The number is : ",i*2)
            time.sleep(2)

    def square(self):
        for i in range(1,6):
            print("The number is : ",i*i)
            time.sleep(2)

o = demo()

t1=Thread(target=o.num())

t2 = Thread(target=o.double())

t3 = Thread(target=o.square())

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()


