# Week 5 Mon Network Socket

---------------
#### :dizzy: **Lab Date :** Feb 9 Monday
#### :alarm_clock: **Due Date :** 2:00 pm Feb 16 (next Monday)   
#### :pencil: Every group member must be present for every check point.
-------------------

> [!NOTE]  
> Today’s lab requires your group to **frequently collaborate with another group** (the neighbor group seated next to you).

## 1. `HTTP server` — Static file host
- [ ] **Get your laptop and Pi both connected to the iot_lab WiFi**

In Pi, use Terminal commands to get IP addresses.

- [ ] **A folder to host static files**

In your Pi, create a folder. Place some files into the folder, such as docs, pictures, videos.

In the Pi terminal

```shell
cd /path/to/your/folder
python3 -m http.server 8000
```

Here, the `http.server` is a module in the Python Standard Library. Its detailed usage in Terminal can be found in https://docs.python.org/3/library/http.server.html#command-line-interface

- [ ] **Access yours Pi server from your laptop**

In your laptop, open a browser, enter such address

```
http://<your_pi_ip>:8000
```

You should be able to access and download files from the folder.

Observe what happened on the Pi Terminal at the same time.

- [ ] **Access your neighbor's Pi server from your laptop**

In your laptop, also try to access your neighbro's server via browswer.

- [ ] Once done, stop the http server in your Pi Terminal.


----------

## 2. `socket` — Low-level networking interface

- [ ] ```socket```  is already in the Pi's Python. It is a low-level tool and can realize simple client-server communication.
- [ ] Your Pi shall act as a server. Your laptop shall act as a client.
- [ ] Establish a simple server-client communication via Python socket. It can send simple string data.
- [ ] You should refer to https://docs.python.org/3/library/socket.html#example

---------

🎉 **Check Point 1**
<br>Show the communication of `HTTP server` & `socket`.

---------


## 3. `ZeroMQ` — High-level networking interface 

```ZeroMQ```  is a high-level networking interface. It can easily configure many-to-many communication. It has multiple communication modes: PUB/SUB, REQ/REP, PUSH/PULL, ...

- [ ] Pi OS doesn't have ```ZeroMQ```. You need to install this package:

```shell
cao@raspberrypiCao:~ $ sudo apt install -y libzmq3-dev
```

```shell
cao@raspberrypiCao:~ $ pip3 install pyzmq --break-system-packages
```

Then go to your Python, check with a simple script
```python
import zmq
print(zmq.__version__)
```
- [ ] **Design a broadcasting system based on following requirements**
  - [ ] The only networking interface package used is ```import zmq``` 
  - [ ] Use the PUB/SUB (Publisher/Subscriber) communication in ZeroMQ
  - [ ] Make arrangement with neighbor group. 
  <br> 1 Groups's Pi act as Publisher, 
  <br> 1 Group's Pi act as Subscriber. 
  <br> Both Group's laptops act as Subscribers. 
  - [ ] Publisher act as a broadcasting station. Connect Pi with **BH1750 Light Sensor**:
  <br> https://learn.adafruit.com/adafruit-bh1750-ambient-light-sensor/overview (Intro)
  <br> https://learn.adafruit.com/adafruit-bh1750-ambient-light-sensor/python-circuitpython (Pi Wiring & Python Code)
  <br> The Publisher broadcasts the "Light Info: " every 10 seconds.
  - [ ] Subscribers receive message.  Pi Subscriber display the info on their I2C OLED screen.

🎉 **Check Point 2**
<br>Both groups demo together and explain the set-up.
