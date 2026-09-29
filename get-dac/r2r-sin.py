import r2r_dac as r2r
import signal_generator as sg
import time
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
try:
        dac = r2r([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        t=0
        while True:
            try:
                voltage = amplitude*sg.get_sin_wave_amplitude(10,t)
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
                t=t+1/sampling_frequency
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()