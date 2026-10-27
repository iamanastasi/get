import mcp3021_driver as driver
import adc_plot as plot
import time 
voltage_values=[]
time_values=[]
duration=5.0
i2c = driver.MCP3021(dynamic_range=5.16)
try:
    start=time.time()
    while(time.time()-start<duration):
        voltage = i2c.get_voltage()
        time_values.append(time.time()-start)
        voltage_values.append(voltage)
    max_voltage=max(voltage_values)
    plot.plot_voltage_vs_time(time_values, voltage_values, max_voltage)
    plot.plot_sampling_period_hist(time_values)
finally:
    i2c.deinit()