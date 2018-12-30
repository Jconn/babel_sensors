import babel_out
import time
from machine import I2C
#id, scl, sda, freq
i2c = I2C(id=-1,scl= 26, sda=27, freq=100000)

# depending on the port, extra parameters may be required
# to select the peripheral and/or pins to use
#mlx90615
addr = 0x5B 
#
obj1_reg = 0x27


i2c.writeto(addr, bytearray([obj1_reg]), stop=False)         # prepare for write 

data = i2c.readfrom(addr, 3)             #read obj temp and crc 
i2c.deinit()

value = (data[1] << 8) | data[0]
temp = ((value-0x2D89)*.02) - 40.01 
babel_out.babel_strstore(str(round(temp, 3)) + "C")
