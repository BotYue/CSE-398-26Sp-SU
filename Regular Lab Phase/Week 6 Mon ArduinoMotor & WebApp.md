# Week 6 Mon: Arduino Motor & WebApp

---------------
#### :dizzy: **Lab Date :** Feb 16 
#### :alarm_clock: **Due Date :** 2:00 pm Feb 23   
#### :pencil: Every group member must be present for every check point.
-------------------


## 1. Basic Setup: Servo → Arduino
- [ ] **Motor set-up**

  The servo motor we use is Smraza 9G Micro Servo Motor 

  The purchase link is https://www.amazon.com/dp/B07L2SF3R4?th=1 

  You can find its wiring and specs on this purchase page.

  Each group uses 2 servo motors.

  Also screw the plastic blade to it, so that you can observe the rotating angle.

- [ ] **Power Supply set-up**

> [!CAUTION]
> Never use a board's Pin (Arduino/Pi/...) to directly power motors. <br> You need to use an external Power Supply.<br>
> Also make sure Common Ground between the external Power Supply and board.

  <img src="Pic/power up.jpg" width="600"/>

  You can use the dual-head screwdriver:

  i) one blade-shaped head to turn power supply voltage; ii) the other cross-shaped head tighten wire insertion  

  <img src="Pic/motor power.png" width="800"/>

- [ ] **Servo → Arduino**

Connect Arduino to 2 motors.

Code the Arduino. Such that you can turn 2 motors at different angles.

🎉 **Check Point 1**

## 2. Web-Controlled Servos

In this task, you will design a web-based control interface that allows a user to command servo motors through a browser. The control pipeline follows this structure:

```
Web Browser (Raspberry Pi)  →  Flask Web App (Raspberry Pi)  →  Arduino  →  Servo Motor
```
