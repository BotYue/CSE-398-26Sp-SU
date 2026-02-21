# Week 7 Mon: Speech Recognition

---------------
#### :dizzy: **Lab Date :** Feb 23
#### :alarm_clock: **Due Date :** 2:00 pm Mar 2   
#### :pencil: Every group member must be present for every check point.
-------------------

## 1. Configure Audio Devices

We have Adafruit Mini USB Microphone: https://www.adafruit.com/product/3367

- [ ] **Configure the microphone.**

Start with checking all audio input:

```shell
cao@raspberrypiCao:~ $ arecord -l
```

You should see ```USB Audio [USB Audio]``` in the list. My terminal shows:

```shell
**** List of CAPTURE Hardware Devices ****
card 0: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

From here, you need to know your USB mic is labeled as ```card 0``` and ```device 0```.


- [ ] **Record a sample audio clip**

Run this command line to record an audio file, here the 2 numbers in ```plughw:0,0 ``` responding to the previous ```card 0``` and ```device 0```. `-t 5` sets 5-second record.

```shell
ffmpeg -f alsa -i plughw:0,0 -t 5 output_feb_21_a.mp4
```

- [ ] **Check the recorded audio clip**
You can play the audio and check whether it has been recorded.

Your Audio output may de default set as the Minitor's HDMI. Check it with:

```shell
sudo raspi-config
```

In "System Options -> S2 Audio" :

<img src="Pic/configaudio.png" width="500"/>

Go to **1 System Options** , Then **S2 Audio** Then adjust settings.

Then run this testing Commond Line, or just play any YouTube video:

```shell
cao@raspberrypiCao:~ $ speaker-test -c2 -twav
```

