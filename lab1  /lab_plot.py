import  matplotlib.pyplot as plt
import math
import numpy as np
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("График  зависимости напряжения на выходе АЦП от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid(True)
    plt.xlim(0, time[len(time)-1])
    plt.ylim(0, max_voltage*1.1)
    plt.show()
def plot_line(time, voltage, max_voltage):
    t_log=np.log10(time)
    v_log=np.log10(voltage)
    log_max=math.log10(max_voltage)
    plt.figure(figsize=(10,6))
    plt.plot(t_log, v_log)
    plt.title(" Линеаризованный график  зависимости напряжения на выходе АЦП от времени")
    plt.xlabel("Логарифсм времени")
    plt.ylabel("Логарифм напряжения")
    plt.grid(True)
    plt.xlim(0, t_log[len(t_log)-1])
    plt.ylim(0, log_max*1.1)
    plt.show()
