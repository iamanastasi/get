import time
import RPi.GPIO as GPIO
class R2R_ADC: 
    def __init__(self, dynamic_range=3.28, compare_time=0.01, verbose=False):
        self.dynamic_range=dynamic_range
        self.verbose=verbose
        self.compare_time=compare_time
        self.bits_gpio=[26,20,19,16,13,12,25,11]
        self.comp_gpio=21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self. bits_gpio, 0)
        GPIO.cleanup()
    def number_to_dac(self, number):
        res=[int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, res)
        return 
    def sequential_counting_adc(self):
        for value in range(256):
            self.number_to_dac(value)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio)==1:
                return(value)
        return 255
    def get_sc_voltage(self):
        number= self.sequential_counting_adc()
        return number*self.dynamic_range/256
    def binsearch(self, min, max):
        return int((max+min)/2 )
    def successive_approximation_adc(self):
        max=256
        min=0
        for value in range(8):
            mid=self.binsearch(min, max)
            self.number_to_dac(mid)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio)==1:
                max=mid
            else:
                min=mid
        return mid
    def get_sar_voltage(self):
        number=self.successive_approximation_adc()
        return number*self.dynamic_range/256
if __name__ == "__main__":
    try:
        adc = R2R_ADC(dynamic_range=3.27,compare_time=0.01, verbose=True)
        
        while True:
            #voltage = adc.get_sc_voltage()
            voltage=adc.get_sar_voltage()
            print(f"Voltage: {voltage:.3f}")
    finally:
        adc.deinit()