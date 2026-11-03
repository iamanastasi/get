import smbus
import time
class MCP3021:
    def __init__(self, dynamic_range,  verbose=False):
        self.bus = smbus.SMBus(1)    
        self.address = 0x4D        
        self.verbose = verbose
        self.dynamic_range = dynamic_range
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число: {number}")
        return number
    def get_voltage(self):
        number= self.get_number()
        return number*self.dynamic_range/1024
if __name__ == "__main__":
    i2c = MCP3021(dynamic_range=5.16, verbose=True)
    try:
        while True:
            voltage=i2c.get_voltage()
            print(f"Voltage: {voltage:.3f}")
            time.sleep(1)
    finally:
        i2c.deinit()