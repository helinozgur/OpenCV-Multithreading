import cv2
import time

class Funcitons():
    def __init__(self):
        self.cap = cv2.VideoCapture('findik.mp4')

    def main(self):
        while True:
            t = time.time()
            res, frame = self.cap.read()
            t2 = time.time() - t
            time.sleep(1 / 30 - t2)
            if res:
                frame = cv2.medianBlur(frame, 301)
                cv2.imshow("frame", frame)
                if cv2.waitKey(27) & 0xFF == ord('q'):

                    break
            else:
                print("\nGECEN SURE:", time.time() - start)
                break
if __name__ == '__main__':
    function_class = Funcitons()
    start = time.time()
    function_class.main()