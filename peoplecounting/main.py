from counterservice import PeopleCounterService
import sys
import time
import numpy as np
import cv2 as cv
import requests
import json

# change URL to match your port
API_URL = "http://localhost:3000/api"
VEHICLE_ID = "1"

def displayFrameAndPostApi(cvFrame, counter):
    cv.imshow('frame', cvFrame)
    cv.waitKey(1)
    print("People counter: {}", counter)
    payload = json.dumps({"people_counter": counter, "vehicle_id": VEHICLE_ID}, separators=(',', ':'))
    header = {"Content-Type": "application/json"}
    try:
        res = requests.post(API_URL, data=payload, headers=header)
    except:
        print("request doesn't work")



if __name__ == "__main__":
    print("Hello, World!")
    if (len(sys.argv) < 2):
        print("Not enough arguments. Usage: python main.py PATH_TO_REF_FRAME")
        exit()
    refFrame = cv.imread(sys.argv[1], cv.IMREAD_GRAYSCALE)
    peopleDetector = PeopleCounterService(cv.VideoCapture(0), refFrame)
    # peopleDetector.registerDetectionCallback(lambda x : print("This is my dummy callback: {}", x))
    peopleDetector.registerDetectionCallback(displayFrameAndPostApi)
    peopleDetector.start()
    # time.sleep(5)
    input("message")
    peopleDetector.stop()
