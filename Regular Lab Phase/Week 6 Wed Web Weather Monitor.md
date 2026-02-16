# Week 6 Wed: Web Weather Monitor

---------------
#### :dizzy: **Lab Date :** Feb 18 
#### :alarm_clock: **Due Date :** 2:00 pm Feb 23   
#### :pencil: Every group member must be present for every check point.
-------------------


## 1. Receive Sensor Data

- [ ] In this task, you will configure the sensor connection, and eventualy receive all these data on the Raspberry Pi side:

1. **Humidity** from the **DHT11** sensor
2. **Temperature** from the **DHT11** sensor
3. **Wind level** from the **MPU-6050 IMU** (let's assume the motion data reflects wind strength)
4. **Light level** from the **BH1750** light sensor

**Wind level definition:**

$$\text{wind level} = |a_x| + |a_y| + |a_z|$$

*(Use accelerometer readings only.)*

- [ ] You are free to configure the wiring for these sensors either directly on the Raspberry Pi or through an Arduino. You may use at most one Arduino board.

- [ ] This time, instead of taking photos of your connections, you should draw an abstract hardware connection diagram. In your diagram, you must explicitly label the communication protocol used for each connection.


🎉 **Check Point 1**
Demo that you can display all 4 data on the Raspberry Pi side at the same time.

---
## 2. Web-Based Monitor

🎉 **Check Point 2**

Each student must present **individually for 30 seconds** to describe personal contributions during this lab, accompanied by questions from the lab staff.<br>
The other two students in the same group must not assist.<br>
Failure to demonstrate meaningful contribution, or answer questions will result in point loss in the corresponding Markdown submission.

