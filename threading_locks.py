import threading
import time
from queue import Queue
from threading import Thread



class Threads():
    def __init__(self):
        self.numbersQueue = Queue()
        self.sum=0
        self.threadLock = threading.Lock()
        self.Thread_addNumber = Thread(name='addFrametoQueue', target=self.addNumber)
        self.Thread_sumNumber = Thread(name='ShowImage', target=self.sumNumber)
        self.Thread_sumNumber2 = Thread(name='BlurImage', target=self.sumNumber)

    def addNumber(self):
        for i in range(10):
            self.numbersQueue.put(i)
            # print("Queue Boyutu:",self.numbersQueue.qsize())

    def sumNumber(self):
        while True:
            if self.numbersQueue.qsize()!=0:
                # self.threadLock.acquire()
                number=self.numbersQueue.get()
                self.sum=self.sum+number
                print("Toplam:",self.sum)
                # self.threadLock.release()
            else:
                break

    def start(self):
        self.Thread_addNumber.start()
        self.Thread_sumNumber.start()
        self.Thread_sumNumber2.start()


if __name__ == '__main__':
    tClass=Threads()
    tClass.start()
    # print("Thread_AddNumber:", tClass.Thread_addNumber.is_alive())
    # print("Thread_SumNumber_1:", tClass.Thread_sumNumber.is_alive())
    # print("Thread_SumNumber_2:", tClass.Thread_sumNumber2.is_alive())
    tClass.Thread_addNumber.join()
    tClass.Thread_sumNumber.join()
    tClass.Thread_sumNumber2.join()
