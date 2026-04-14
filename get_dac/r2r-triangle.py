import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 1
signal_freq = 1
sampling_freq = 10

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    while True:
        dac.set_voltage(amplitude * sg.get_triangle_wave_amplitude(signal_freq, time.monotonic()))
        sg.wait_for_sampling_period(sampling_freq)
finally:
    dac.deinit()