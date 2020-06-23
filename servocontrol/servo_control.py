from periphery import GPIO
import threading
import time
from debugmessages import *


class Servo:
    def __init__(self, pin, min_pulse=1, max_pulse=2, frequency=50):
        self.debug = DebugMessages(self)
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.mid_pulse = (min_pulse + max_pulse) / 2
        self.looping = True
        self.pin = GPIO(pin, "out")
        self.frequency = frequency
        self.millis = self.mid_pulse
        self.old_millis = -1
        self.thread = threading.Thread(target=self.loop, args=())
        self.thread.start()

    def __del__(self):
        self.looping = False

    def loop(self):
        while self.looping:
            if self.old_millis != self.millis:
                self.debug.info(str(self.looping))
                self.pin.write(True)
                time.sleep(self.millis / 1000)
                self.pin.write(False)
                time.sleep(((1000 / self.frequency) - self.millis) / 1000)
                self.old_millis = self.millis

    def set_angle(self, angle):
        if 180 >= angle >= 0:
            self.millis = ((angle - 90) / 90) * (self.mid_pulse - self.min_pulse) + self.mid_pulse
        else:
            raise ValueError("Angle out of bounds!")
