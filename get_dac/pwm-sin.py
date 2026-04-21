import RPi.GPIO as GPIO
import signal_generator as sg
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.p = GPIO.PWM(self.gpio_pin, self.pwm_frequency)

    def deinit(self):
        self.p.stop()
        GPIO.cleanup()

    def set_voltage(self, voltage):
        self.p.start(voltage / self.dynamic_range * 100)

amplitude = 1
signal_freq = 1
sampling_freq = 10

try:
    dac = PWM_DAC(12, 2500, 3.297, True)
    while True:
        dac.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_freq, time.monotonic()))
        sg.wait_for_sampling_period(sampling_freq)
finally:
    dac.deinit()