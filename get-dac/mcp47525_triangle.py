import mcp4725_driver as mcp
import triangle_generator as tg

try:
    dac = mcp.MCP4725( 3.183, False)
    t=0.0
    amplitude = float(input("Введите амплитуду в Вольтах: "))
    signal_frequency = int(input("Введите частоту сигала в Герцах: "))
    sampling_frequency = int(input("Введите частоту дискретизации в Герцах: "))
    while True:
        try:
            voltage = amplitude*tg.get_sin_wave_amplitude(signal_frequency,t)
            dac.set_voltage(voltage)
            tg.wait_for_sampling_period(sampling_frequency)
            t=t+1/sampling_frequency
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    dac.deinit()
