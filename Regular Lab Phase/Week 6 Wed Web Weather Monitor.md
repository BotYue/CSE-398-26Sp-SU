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

$$\text{wind level} =  \text{factor} \times (|a_x| + |a_y| + |a_z|)$$

*(Use accelerometer readings only. "factor" is a scaling constant that you can define.)*

- [ ] You are free to configure the wiring of these sensors<br>Either directly on the Raspberry Pi or through an Arduino. <br>You may use at most one Arduino board.

- [ ] This time, instead of taking photos of your connections, you should draw **an abstract hardware connection diagram**.<br> In your diagram, you must explicitly label the communication protocol used for each connection.

> [!NOTE]
> Both MPU-6050 IMU and BH1750 have supported Python library:
> - **MPU-6050:** https://github.com/adafruit/Adafruit_CircuitPython_MPU6050
> - **BH1750:** https://github.com/adafruit/Adafruit_CircuitPython_BH1750
>  
> When you install extra Python library in Rasp Pi, you should always do `--break-system-packages`. Example seen in [previous adafruit_ssd1306 Python package install](Week%204%20Mon%20I2C.md#2-i2c---a-status-monitor)

> [!TIP]
> A key feature of I²C is that it allows multiple devices to share the same bus.

🎉 **Check Point 1**

Demo that you can display all 4 data values on the Raspberry Pi side at the same time.

---
## 2. Web-Based Monitor via Agentic CLI Programming

- [ ] In this task, you will use agentic command-line (CLI) programming on the Raspberry Pi to
  assist with building a web-based monitor for logging and displaying all sensor data.

- [ ] If you are unable to set up an agentic CLI tool, you may instead use a chat-window–based AI assistant.

- [ ] Prompts used should be documented in your Markdown report.




🎉 **Check Point 2**

Each student must present **individually for 30 seconds** to describe personal contributions during this lab, accompanied by questions from the lab staff.<br>
The other two students in the same group must not assist.<br>
Failure to demonstrate meaningful contribution, or answer questions will result in point loss in the corresponding Markdown submission.

