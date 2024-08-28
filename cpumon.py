#  Created by SRDC

import os
import time

while True:
    temperature = float(os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C",""))
    voltage = float(os.popen('vcgencmd measure_volts core').readline().replace("volt=","").replace("V",""))
    print(temperature, "°C", "|", voltage, "V")
    time.sleep(1)
