# RPi CPU Temperature Monitor

### Create file

```
sudo nano cpumon.py
```

### Copy code below

```
#  python monitor_cpu.py

import os
import time

while True:
    temperature = float(os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C",""))
    voltage = float(os.popen('vcgencmd measure_volts core').readline().replace("volt=","").replace("V",""))
#   print("Temp: ", temperature, "°C", " @ ", voltage, "V")
#   print("Temp.: ", temperature, "°C", "|", "Volt.: ", voltage, "V")
    print(temperature, "°C", "|", voltage, "V")
#   print("Temperature: ", temperature, "°C", "\tVoltage: ", voltage, "V")
    time.sleep(1)
```

### Save and Exit

CTRL+X -> Y -> ENTER
