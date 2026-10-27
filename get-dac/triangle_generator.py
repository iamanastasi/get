import time
import math
def get_sin_wave_amplitude(freq, time):
    return 1/math.pi*(math.asin(math.sin(2*math.pi*freq*time)))+0.5
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)