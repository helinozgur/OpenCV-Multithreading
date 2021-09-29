import sys
import cv2
from queue import Queue
from threading import Thread
import time

class Thread_Funcitons():
    def __init__(self):
        self.cap = cv2.VideoCapture('findik.mp4')
        self.frameQueue = Queue()
        self.resultQueue = Queue()
        self.res=True
        self.Thread_addFrame = Thread(name='addFrametoQueue', target=self.addFrametoQueue)
        self.Thread_ShowImg = Thread(name='ShowImage', target=self.showImage)
        self.Thread_BlurImg = Thread(name='BlurImage', target=self.blurImg)
        self.Thread_BlurImg2 = Thread(name='BlurImage', target=self.blurImg)
        self.Thread_BlurImg3 = Thread(name='BlurImage', target=self.blurImg)
        self.Thread_BlurImg4 = Thread(name='BlurImage', target=self.blurImg)
        self.Thread_BlurImg5 = Thread(name='BlurImage', target=self.blurImg)
    def addFrametoQueue(self):
        while True:
            # frame=self.cap
            t=time.time()
            self.res, frame = self.cap.read()
            t2=time.time()-t
            time.sleep(1/30-t2)
            if self.res:
                try:
                    self.frameQueue.put(frame, block=False)
                except:
                    print("Frame eklenmedi!")
                print("Queue Boyutu:", self.frameQueue.qsize())
                if not self.Thread_ShowImg.is_alive():
                    sys.exit()
            else:
                break

    def blurImg(self):
        while True:
            frame=self.frameQueue.get()
            result=cv2.medianBlur(frame,301)
            self.resultQueue.put(result, block=False)
            self.frameQueue.task_done()
            if not self.Thread_ShowImg.is_alive():
                sys.exit()

    def showImage(self):
        while True:
            if self.res:
                frame = self.resultQueue.get()
                # frame = cv2.resize(frame, None, None, .20, .20)
                cv2.imshow("frame", frame)
                if cv2.waitKey(27) & 0xFF == ord('q'):
                    sys.exit()
            else:
                print("\nGECEN SURE:", 10.287829685211182)
                break

    def StartThreads(self):
        self.Thread_addFrame.start()
        self.Thread_ShowImg.start()
        self.Thread_BlurImg.start()
        self.Thread_BlurImg2.start()
        self.Thread_BlurImg3.start()
        self.Thread_BlurImg4.start()
        self.Thread_BlurImg5.start()

if __name__ == '__main__':
    Thread_Class = Thread_Funcitons()
    start = time.time()
    Thread_Class.StartThreads()
    print("\nThread_ShowImg:", Thread_Class.Thread_ShowImg.is_alive())
    print("Thread_start:", Thread_Class.Thread_addFrame.is_alive())
    Thread_Class.Thread_addFrame.join()
    Thread_Class.Thread_ShowImg.join()
    Thread_Class.Thread_BlurImg.join()
    Thread_Class.Thread_BlurImg2.join()
    Thread_Class.Thread_BlurImg3.join()
    Thread_Class.Thread_BlurImg4.join()
    Thread_Class.Thread_BlurImg5.join()