import sys
import cv2
from queue import Queue
from threading import Thread
import time

def blurFunction(frameQueue):
    while True:
        img = frameQueue.get()
        blur = cv2.blur(img, (10, 10))
        time.sleep(0.05)
        blurQueue.put(blur,block=False)
        # cv2.imshow("frame", blur)
        frameQueue.task_done()
        if not Thread_ShowImg.is_alive():
            sys.exit()


def showImage(blurQueue):
    while True:
        blurimg = blurQueue.get()
        cv2.imshow("frame", blurimg)
        blurQueue.task_done()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sys.exit()


def addFrametoQueue(cap):
    c = 0
    while True:
        res, frame = cap.read()
        try:
            frameQueue.put(frame,block=False)
            c += 1
        except:
            print("Frame eklenmedi!")
        # frameQueue.put(frame,block=False)
        print(frameQueue.qsize())
        if not Thread_ShowImg.is_alive():
            sys.exit()

if __name__ == '__main__':
    frameQueue = Queue()
    blurQueue=Queue()
    cap = cv2.VideoCapture(0)
    Thread_start = Thread(name='addFrametoQueue', target=addFrametoQueue, args=(cap,))
    Thread_blur_1 = Thread(name='BlurThread', target=blurFunction, args=(frameQueue,))
    Thread_ShowImg = Thread(name='ShowImage', target=showImage, args=(blurQueue,),daemon=False)

    Thread_start.start()
    Thread_blur_1.start()
    Thread_ShowImg.start()
    print("Thread_ShowImg:",Thread_ShowImg.is_alive())
    print("Thread_start:",Thread_start.is_alive())
    print("Thre_blur_1:",Thread_blur_1.is_alive())
    Thread_start.join()
    Thread_blur_1.join()
    Thread_ShowImg.join()
