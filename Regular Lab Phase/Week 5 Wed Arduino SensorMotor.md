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
<br>The usage of this IMU is compatible as the one on  the Adafruit website:
<br>https://learn.adafruit.com/mpu6050-6-dof-accelerometer-and-gyro/overview 
<br>https://learn.adafruit.com/mpu6050-6-dof-accelerometer-and-gyro/python-and-circuitpython

🎉 **Check Point 1**
<br>Show the communication of `HTTP server` & `socket`.
<br>Students will be asked regarding to commands/functions, fail to answer receive 50% credit.

---------


## 3. Motor Integration



- [ ] 
🎉 **Check Point 2**
<br>Both groups demo together and explain the set-up.
<br>Student who fails to explain receive 50% credit.
