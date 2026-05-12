import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

try:
    max_voltage = 3.295
    adc = R2R_ADC(max_voltage, 0.01)
    v = []
    t = []
    duration = 5.0

    start_time = time.monotonic()
    moment_time = start_time

    while moment_time - start_time < duration:
        v.append(adc.get_sar_voltage())
        t.append(moment_time-start_time)
        moment_time = time.monotonic()

    adc.deinit()
    plot_voltage_vs_time(t, v, max_voltage)
    plot_sampling_period_hist(t)
finally:
    adc.deinit()
