# RPi CPU Temperature Monitor

## 1. <em>(Optional)</em> - Update, Upgrade and Restart your Raspberry Pi 

### Update:
```
sudo apt update
```
### Upgrade:
```
sudo apt upgrade -y
```
### Restart
```
sudo shutdown -r 0
```

### Check Python Version

```
python --version
```

### Update Python to the latest version
```
Update Python
```

### Install Python

```
Install Python
```

## 2. Download or Create script

### Download script
```
Download script
```

### Create file

```
sudo nano cpumon.py
```

### Copy code below

```
import os
import time

while True:
    temperature = float(os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C",""))
    voltage = float(os.popen('vcgencmd measure_volts core').readline().replace("volt=","").replace("V",""))
    print(temperature, "°C", "|", voltage, "V")
    time.sleep(1)
```

### Save and Exit

CTRL+X -> Y -> ENTER

### Run the script

```
sudo python cpumon.py
```

### Stop the script

CTRL+C
