# This module implements timer based functionality for two Chip-8 timers
# Delay timer -
# Sound timer -

import time
import threading
from constants import *

class Timer(threading.Thread):
    def __init__(self, value=0x0):
        super().__init__(self)
        self.timereg = value

    def set_timer(self, value):
        self.timereg = value & BYTEMASK

    def get_timer(self):
        return self.timereg & BYTEMASK

    def run(self):
        while True:
            time.sleep(TICK_16ms)
            if self.timereg != 0:
                self.timereg -= 1

