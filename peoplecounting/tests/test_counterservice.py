"""
© Copyright CERN 2019.  All rights reserved. This software is released under a CERN proprietary
software licence. Any permission to use it shall be granted in writing. Requests shall be
addressed to CERN through mail-KT@cern.ch

Author: Anastasiia Riabchikova CERN EN/SMM/MRO
"""

from .context import counterservice
from counterservice import PeopleCounterService
import pytest
import time
import numpy as np

class MockVideoDevice:
    def __init__(self):
        pass
    def read(self):
        return (True, np.zeros((640,480,3), np.uint8))

def test_start_and_stop_the_service():
    sut = PeopleCounterService(MockVideoDevice())
    sut.start()
    sut.start()
    sut.stop()
    sut.stop()
    sut.registerDetectionCallback(lambda x : print("Peron detected: {}", x))
    sut.start()
    time.sleep(2)
    sut.stop()
