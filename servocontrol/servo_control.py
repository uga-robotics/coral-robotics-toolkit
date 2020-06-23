from periphery import PWM


class Servo:
    def __init__(self, bank, channel=0, min_pulse=1, max_pulse=2, frequency=50):
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.mid_pulse = (min_pulse + max_pulse) / 2
        self.pwm = PWM(bank, channel)
        self.pwm.frequency = frequency
        self.pwm.enable()

    def __del__(self):
        self.pwm.close()

    def set_angle(self, angle):
        if 180 >= angle >= 0:
            millis = ((angle - 90) / 90) * (self.mid_pulse - self.min_pulse) + self.mid_pulse
            self.pwm.duty_cycle = millis / 50
        else:
            raise ValueError("Angle out of bounds!")
