### Lab 6 Work Log

--------------------

##### Lab topic: Basic I2C interface

##### Group member: Yue Cao, Jiamin Zhao, Duane Marcy

[ Note: This is a template showing you how to format a Markdown file to record lab work. ]

--------------------------------

##### Jan/10, Mon 12:00 - 12:30 pm

[ Note we recommend you pause to log your progress within 30 minutes, even every 15 minutes, or any time you made significant progress.]

* I try to test a soil sensor with I2C conection to my Pi 5
   [ Note: It is OK if there are minor grammar issues or typos. The content just needs to be understandable by others..]

* I selected "Adafruit STEMMA Soil Sensor" from the shelf. I looked up online and found its document on https://www.adafruit.com/product/4026 
   [ Note: keep all useful website links in the log..]

* I checked its pinout connection on https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/pinouts . 
  It is:

  * black: GND
  * red: 3-5 V DC
  * white: I2C SDA
  * green: I2C SCL

  [ Note: carefully record all you hardware info, so that you can re-create.]

* I try this in shell:
  ```bash
  ls /dev/i2c
  ```
  it shows 2 bus.

  [ Note: carefully record everything you tried in shell command line. As well as output. Command line can use bash or shell code format in Markdown. ]
  
* In shell, I can use ```i2cdetect -y 11``` or ```i2cdetect -y 12``` , but the address at 0x36 is  --

  It seems not working.

  [ Note: if you encountered issues, also record it and how it happened.]

-----------------------

##### Jan/10, Mon 12:30 - 1:00 pm

* I check with ChatGPT with preivous issue. It told me to do such in shell:
  ```bash
  sudo raspi-config
  ```

​	It poped out a GUI.

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

[ Note: you can specify the code format for code block (Python/C/shell/...)..]

* It works! 

------------------------

##### Everything was verified by lab staff on Jan/10, Mon 1:30 pm

