# Week 5 Wed Arduino SensorMotor

---------------
#### :dizzy: **Lab Date :** Feb 9 Monday
#### :alarm_clock: **Due Date :** 2:00 pm Feb 16 (next Monday)   
#### :pencil: Every group member must be present for every check point.



### **Introduction**

In this lab, we will integrate the sensors and motors with the Pi 5. While sensors and motors can be directly connected to the Pi 5, the better way is to add an Arduino as an intermediate device.

Using the Arduino as an intermediate has such advantages:

1. **Better Task Allocation:** The Arduino will handle simple looping tasks. This keeps the Raspberry Pi code simpler and focus on other tasks.
2. **Better Timing:** The Arduino has better timing mechanism than the Raspberry Pi, such as the `millis()` function.
3. **Hardware Isolation:** Motors typically draw high currents, and beginners often make wiring mistakes. Using an Arduino as an intermediate layer helps isolate the Raspberry Pi from sudden high current. (**is about damaging a Pi or damaging a cheap Arduino!**)

## 1.  Sensor Integration

In this task, we use use an IMU as a sensor, and set a communication path: **Sensor → Arduino → Raspberry Pi**

- [ ] **Get any Arduino board that is 3.3 V logic**
<br>Connect Arduino to your own laptop
<br>Check Arduino uploading using the simplest example -- Blink

- [ ] **Set up MPU6050 IMU**

The IMU we purchased is: 
Pre-Soldered SHILLEHTEK MPU6050,<br>
https://www.amazon.com/Pre-Soldered-Accelerometer-Raspberry-Compatible-Arduino/dp/B0BMY15TC4 
<br>The usage of this IMU can be found on the Adafruit website:
<br>https://learn.adafruit.com/mpu6050-6-dof-accelerometer-and-gyro/overview 
<br>https://learn.adafruit.com/mpu6050-6-dof-accelerometer-and-gyro/python-and-circuitpython

- [ ] **Code the IMU**

In your Arduino IDE, code the IMU, print the sensor readings to the Serial Monitor.
<br>There should be 6 data: 3 Accelerometer data, 3 Accelerometer data
<br>Move your IMU around, see if the sensor readings make sense.

- [ ] **Read Arduino data in Pi**

Make sure your IMU code is successfully compiled and uploaded to the Arduino.
  <br>Disconnect the USB cable from your computer, and then reconnect USB from the Arduino to the Raspberry Pi.
  <br>The Arduino should continue running the previously uploaded IMU code.
  <br>On the Raspberry Pi, identify the serial port used by the Arduino (e.g., `/dev/ttyACM0`).
  
   ```shell
  ~ $ ls /dev/ttyACM*
  ```

  <br>Verify that IMU data is being received on the Raspberry Pi using the `serial` library.

  ```python
import serial

PORT = '/dev/ttyACM0'
BAUD_RATE = 115200

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)

while True:
    line = ser.readline().decode(errors='ignore').strip()
    if line:
        print(line)
```
🎉 **Check Point 1**
<br>Students will be asked regarding to the implementation, fail to answer receive 50% credit.


## 2.  **Deisgn an Earthquake Alarm System** 
Deisgn using such way "Sensor → Arduino → Raspberry Pi"
  - [ ] The Raspberry Pi program operates in **two modes** and print to the OLED or LCD screen of Raspberry Pi:
    - **Normal Mode:** no strong vibration is detected; the Raspberry Pi continuously prints the current time and system status (such as temperature).
    - **Alarm Mode:** strong vibration is detected; normal status printing is interrupted, and the Raspberry Pi prints alarm messages and detailed IMU data (accelerometer and gyroscope). When vibration stops, the program returns to Normal Mode.
    - The screen is connected directly to Raspberry Pi GPIO; The IMU is connected via Arduino then to Raspberry Pi.
    - "Strong vibration": feel free to choose accelerometer/gyroscope thresholds that make sense based on your observations.

🎉 **Check Point 2**
<br>Students will be asked regarding to the implementation and contribution, fail to answer receive 50% credit.

---------
> [!NOTE]  
> You should include lab procedures, all Arduino code, all Rasp Pi Python code in your Markdown
> 
> If you don't include hardware connection photos. You should clearly describe the pin-to-pin connections in text.

> [!NOTE]  
> **Motor Integration** will be introduced next week, together with web app design.

