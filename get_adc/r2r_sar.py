import r2r_adc as r2r
import time 
import adc_plot as plot
voltage_values=[]
time_values=[]
duration=5.0
try:
    adc = r2r.R2R_ADC(dynamic_range=3.27,  compare_time=0.001)
    start=time.time()
    while(time.time()-start<duration):
        voltage = adc.get_sar_voltage()
        time_values.append(time.time()-start)
        voltage_values.append(voltage)
    max_voltage=max(voltage_values)
    plot.plot_voltage_vs_time(time_values, voltage_values, max_voltage)
    plot.plot_sampling_period_hist(time_values)
finally:
    adc.deinit()