from counterservice import PeopleCounterService
import time
import numpy as np
import cv2 as cv

def displayFrame(cvFrame):
    cv.imshow('frame', cvFrame)
    cv.waitKey(1)

if __name__ == "__main__":
    print("Hello, World!")
    peopleDetector = PeopleCounterService(cv.VideoCapture(0))
    # peopleDetector.registerDetectionCallback(lambda x : print("This is my dummy callback: {}", x))
    peopleDetector.registerDetectionCallback(displayFrame)
    peopleDetector.start()
    # time.sleep(5)
    input("message")
    peopleDetector.stop()



