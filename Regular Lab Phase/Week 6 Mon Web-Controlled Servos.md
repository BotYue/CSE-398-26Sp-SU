# Week 6 Mon: Web-Controlled Servos

---------------
#### :dizzy: **Lab Date :** Feb 16 
#### :alarm_clock: **Due Date :** 2:00 pm Feb 23   
#### :pencil: Every group member must be present for every check point.
-------------------


## 1. Basic Setup: Servo and Arduino

In this task, you will do such basic set-up


$$\mathrm{Arduino  →  Servo Motor}$$

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
> [!CAUTION]
> Never connect motor wires directly to the Raspberry Pi, even through a breadboard.
>
> You can use two separate breadboards for the Raspberry Pi and the Arduino.

- [ ] In this task, you will design a web-based control interface that allows a user to command two servo motors through a browser. The pipeline is:


$$\mathrm{Web Browser (Raspberry Pi)  →  Flask Web App (Raspberry Pi)  →  Arduino  →  Servo Motor}$$

- [ ] The web user interface should be clear and intuitive for end users, using appropriate interface elements such as sliders or similar controls.

- [ ] AI tools are allowed in development.

---

Suggestion for accelerating your development: **split the work into two phases**:

#### Phase 1 — Raspberry-Pi-Only Test (No Arduino, No Servo)

In this phase, you develop and test the Flask web application without any hardware connected. User actions in the browser send commands to the Flask server, and **two servo angle values** are printed to the terminal instead of being sent to an Arduino.

**Expected Terminal output example:**

```shell
[Send to Arduino] 90, 135
[Send to Arduino] 90, 115
[Send to Arduino] 60, 115
```

#### Phase 2 — Hardware-Integrated Test (with Arduino & Servo)

In this phase, the Flask web application sends two servo angle commands to the Arduino through serial communication (`import serial` in Python). The Raspberry Pi and Arduino are connected via USB. The Arduino receives the commands and drives each servo motor to the corresponding angle.


---

🎉 **Check Point 2**

Each student must present **individually for 30 seconds** to describe personal contributions during this lab, accompanied by questions from the lab staff.<br>
The other two students in the same group must not assist.<br>
Failure to demonstrate meaningful contribution, or answer questions will result in point loss in the corresponding Markdown submission.

