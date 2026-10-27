import  matplotlib.pyplot as plt
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
def plot_sampling_period_hist(time):
    deltas=[]
    for i in range(len(time)-1):
        deltas.append(time[i+1]-time[i])
    plt.figure(figsize=(10,6))
    plt.hist(deltas)
    plt.title("Гистограмма")
    plt.xlabel("Время, с")
    plt.grid(True)
    plt.xlim(0, 0.06)
    plt.show()