from r2r_adc import R2R_ADC

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.295, 0.01, True)

        while True:
            print(f"\rНапряжение: {adc.get_sar_voltage():.03f}", end="", flush=True)
    finally:
        adc.deinit()
