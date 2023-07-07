"""
© Copyright CERN 2023.  All rights reserved. This software is released under a CERN proprietary
software licence. Any permission to use it shall be granted in writing. Requests shall be
addressed to CERN through mail-KT@cern.ch

Author: Anastasiia Riabchikova CERN EN/SMM/MRO
"""

from . import helpers
from threading import Thread
import time
import numpy as np
import cv2 as cv

BINARY_THRESHOLD_LOW = 80
BINARY_THRESHOLD_UP = 255
NORM_THRESHOLD = 50000 # could be tuned if needed...

class PeopleCounterService:
    def __init__(self, captureDevice, refFrame):
        print("init")
        self.__captureDevice = captureDevice
        self.__refFrame = refFrame
        self.__worker = Thread()
        self.__stop = True
        self.__cb = None
        self.__personDetected = False
        self.__peopleCounter = 0
    def start(self):
        print("start")
        self.__stop = False
        if (self.__worker.is_alive()):
            print("already running")
            return
        self.__worker = Thread(target = self.__workerAsync)
        self.__worker.start()
    def stop(self):
        print("stop")
        self.__stop = True
        if (not self.__worker.is_alive()):
            print("already stopped")
            return
        self.__worker.join()
    def registerDetectionCallback(self, cb):
        print("callback registered, let's call it already ...")
        self.__cb = cb
    def __workerAsync(self):
        print("Worker starts ... ")
        while(not self.__stop):
            print("loop")
            cvFrame = self.__frameCapture()
            print ("shape: {} vs {}",cvFrame.shape, self.__refFrame.shape)
            normDiff = cv.norm(cv.absdiff(cvFrame, self.__refFrame))
            print("the value of the norm matrix", normDiff)
            if (normDiff > NORM_THRESHOLD and not self.__personDetected):
                print("new person detected")
                self.__personDetected = True
                self.__peopleCounter += 1
            elif (normDiff < NORM_THRESHOLD and self.__personDetected):
                print("person no longer detected")
                self.__personDetected = False
            if (self.__cb != None):
                self.__cb(cvFrame, self.__peopleCounter)
            time.sleep(1)
        print("Worker stops ... ")
    def __frameCapture(self):
        ret, frame = self.__captureDevice.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?)")
            return None
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        ret,frame = cv.threshold(frame,BINARY_THRESHOLD_LOW,BINARY_THRESHOLD_UP,cv.THRESH_BINARY)
#        cv.imwrite("refFrame.png",frame)
        return frame
