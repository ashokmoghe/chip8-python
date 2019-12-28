# This module implements timer based functionality for two Chip-8 timers
# Delay timer -
# Sound timer -

import time
from constants import *

class Timer():
    def __init__(self):
        self.timereg = 0x0

    def set_timer(self, byetval):
        self.timereg = byetval & BYTEMASK

    def get_timer(self):
        return(self.timereg & BYTEMASK)


def tick_function(name, dt):
    while True:
        time.sleep(TICK_16ms)
        if (dt.timereg !=0):
            dt.timereg -= 1

