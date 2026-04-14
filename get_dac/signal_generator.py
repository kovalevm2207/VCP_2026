import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1)/2

def wait_for_sampling_period(sampling_freq):
    time.sleep(1 / sampling_freq)

def get_triangle_wave_amplitude(freq, time):
    period = 1.0 / freq
    t_norm = (time % period) / period
    return 2*abs(t_norm - 0.5)
