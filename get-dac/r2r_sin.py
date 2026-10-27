import r2r_dac as r2r
import signal_generator as sg
try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, False)
    t=0.0
    amplitude = float(input("Введите амплитуду в Вольтах: "))
    signal_frequency = int(input("Введите частоту сигала в Герцах: "))
    sampling_frequency = int(input("Введите частоту дискретизации в Герцах: "))
    while True:
        try:
            voltage = amplitude*sg.get_sin_wave_amplitude(signal_frequency,t)
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
            t=t+1/sampling_frequency
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    dac.deinit()