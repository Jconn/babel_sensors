import babel_out
import time
from machine import Pin 

def do_data(cycles):
    clk.value(0)
    prev_value = 0
    while data.value() != 0 or prev_value != 1:
        prev_value = data.value()
    result = 0
    for i in range(cycles):
        clk.value(1)
        clk.value(0)
        if i < 24:
            result = (result | (data.value() << (23 - i)))
    time.sleep(.01)
    return result
data = Pin(27, Pin.IN)
clk = Pin(26, Pin.OUT)


r1 = do_data(26) 
r1 = 1.0*r1/(1<<24 -1) * 3.26/2 
r2 = do_data(25)
clk.value(1)
babel_out.babel_strstore( str(r1) + "," + str(r2) + " adc2")

