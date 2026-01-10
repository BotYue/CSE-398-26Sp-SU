> \[!NOTE]
> This is a template showing you how to format a Markdown file to record lab work. 

### Week 6 Wed I2C Interface

##### Group members: Yue Cao, Jiamin Zhao, Duane Marcy
##### All check points verfied on Feb 30


--------------------------------

##### Feb 30, Mon 12:00 - 12:30 pm

> \[!NOTE]
> Note we recommend you pause to log your progress within 30 minutes, even every 15 minutes, or any time you made significant progress.

* I try to test a soil sensor with I2C conection to my Pi 5

> \[!NOTE]
>  It is fine if there are grammar issues or typos. Just make your tech content understandable.

* I selected "Adafruit STEMMA Soil Sensor" from the shelf. I looked up online and found its document on https://www.adafruit.com/product/4026 
> \[!NOTE]
> Also keep all useful website links in the log..

* I checked its pinout connection on https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/pinouts . 
  It is:

  * black: GND
  * red: 3-5 V DC
  * white: I2C SDA
  * green: I2C SCL

> \[!NOTE]
> Note: carefully record all you hardware info, so that you can re-make.

* I try this in shell:
  ```bash
  ls /dev/i2c
  ```
  it shows 2 bus.

> \[!NOTE]
> carefully record everything you tried in shell command line. As well as output. Command line can use bash or shell code format in Markdown. 
  
* In shell, I can use ```i2cdetect -y 11``` or ```i2cdetect -y 12``` , but the address at 0x36 is  --

  It seems not working.

> \[!NOTE]
> Note: if you encountered issues, also record it and how it happened.

-----------------------

##### Jan/10, Mon 12:30 - 1:00 pm

* I check with ChatGPT with preivous issue. It told me to do such in shell:
  ```bash
  sudo raspi-config
  ```

​	It poped out a GUI.

> \[!NOTE]
> Note: you are free to use AI tools. If you use AI tools, should state it.
  
* I can now navigate in the GUI and enable I2C in here.
* I tried this in shell:
  ```ls /dev/i2c-*``` , I saw new I2C device, named i2c-1
  then in shell do ```i2cdetect -y 1```, I see the pop out is all dashed line, expect a single number 28 located at 8-20 (column-row).
* I asked ChatGPT how to check the I2C connection is Python.

 ```python
 import smbus
 import time
 
 I2C_BUS = 1
 DEVICE_ADDR = 0x28
 
 CHIP_TO_REG = 0x00
 
 bus = smbus.SMBus(I2C_BUS)
 chip_id = bus.read_byte_data(DEVICE_ADDR, CHIP_TO_REG)
 print(chip_id)
 ```

* It works! 

------------------------

#### Convert to .PDF then submit to BlackBoard
