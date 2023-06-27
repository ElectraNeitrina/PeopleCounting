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

class PeopleCounterService:
    def __init__(self, captureDevice):
        print("init")
        self.__captureDevice = captureDevice
        self.__worker = Thread()
        self.__stop = True
        self.__cb = None
        self.__cvFrame = None
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
            self.__frameCapture()
            if (self.__cb != None):
                self.__cb(self.__cvFrame)
            time.sleep(1)
        print("Worker stops ... ")
    def __frameCapture(self):
        ret, frame = self.__captureDevice.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?)")
            return
        self.__cvFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
