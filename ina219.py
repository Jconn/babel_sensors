import babel_out
import time
from machine import Pin 
import time
from machine import I2C
i2c_addr = 0x40
#id, scl, sda, freq
i2c = I2C(id=-1,scl= 27, sda=26, freq=100000)          # create I2C peripheral at frequency of 400kH


i2c.writeto(i2c_addr, bytearray([0x00, 0x39, 0x9F]))         # initialize the dumb thing

i2c.writeto(i2c_addr, bytearray([0x05, 4096 >> 8, 4096 & 0xFF]))         # initialize the dumb thing
i2c.writeto(i2c_addr, bytearray([0x04]))         # initialize the dumb thing
time.sleep(.05)
raw_current = i2c.readfrom(i2c_addr, 2)             # read 4 bytes from slave with 7-bit address 42
ma_current = raw_current[0] << 8 | raw_current[1]
babel_out.babel_strstore(str(round(ma_current/10.0, 3)) + "mA")
i2c.deinit()
