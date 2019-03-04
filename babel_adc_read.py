import babel_out
import time
# create an output pin on pin #0

adc_val = babel_out.babel_get_adc()
temp = (adc_val - 500)/10.
babel_out.babel_strstore(str(round(temp, 3)) + "C")
time.sleep(.1)
