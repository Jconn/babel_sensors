import babel_out
import time
from machine import I2C
#id, scl, sda, freq
i2c = I2C(id=-1,scl= 26, sda=27, freq=100000)          # create I2C peripheral at frequency of 400kHz
# depending on the port, extra parameters may be required
# to select the peripheral and/or pins to use

read_msb_addr = 0x73 >> 1
read_lsb_addr = 0x71 >> 1
write_addr = 0x70 >> 1
init_write = 0x06


i2c.writeto(write_addr, bytearray([init_write]))         # initialize the dumb thing

lsb = i2c.readfrom(read_lsb_addr, 1)             # read 4 bytes from slave with 7-bit address 42
msb = i2c.readfrom(read_msb_addr, 1)             # read 4 bytes from slave with 7-bit address 42
i2c.deinit()

value = msb[0] << 1 | lsb[0]

babel_out.babel_strstore(str(round(value, 3)) + "Lumens")
