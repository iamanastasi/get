import mcp4725_driver as mcp
import signal_generator as sg

try:
    dac = mcp.MCP4725( 4.2, False)
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
