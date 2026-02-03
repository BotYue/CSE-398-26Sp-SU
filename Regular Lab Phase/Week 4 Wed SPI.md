# Week 4 Wed SPI

---------------
#### :dizzy: **Lab Date :** Feb 4 Wednesday
#### :alarm_clock: **Due Date :** 2:00 pm Feb 9 (next Monday)   
#### :pencil: Every group member must be present for every check point.
-------------------

## 1. SPI - Basic set-up
- [ ] **Hardware intro**
  <br>You will play with a SPI based LCD display. 
  <br>It is this product:
  <br>Waveshare 2inch Mini LCD Screen - 240x320 Resolution IPS LCD Display, 262K RGB Color, Embedded ST7789VW Driver, SPI Interface.
  <br>https://www.amazon.com/dp/B082GFTZQD?th=1
- [ ] **Hardware connection**
  <br>Follow the official guide by Waveshare to connect 
  <br> https://www.waveshare.com/wiki/2inch_LCD_Module
  <br> Or directly refer to the pin-connection image below.

| Note: Your wire coloring may be different | 
|---------------------|
| <img src="Pic/lcd_wiring.png" width="700"> |

 

- [ ] **Pi OS Configuration**
  <br>You need to turn on the SPI in the Pi OS firstly.
  <br>Go to your top left menu, you can find ```Preferences``` -> ```Raspberry Pi Configuration```.
    <img src="Pic/SPIturnOn.png" width="600"/>

  <br> At this point, you may already see the LCD backlight turn on (although no image displayed yet).


## 2. SPI - Simple image display
- [ ] **Don't** follow the software setup in the official guide by Waveshare. It overcomplicates things.
- [ ] Download the example code from Waveshare
      
```bash
wget https://files.waveshare.com/upload/8/8d/LCD_Module_RPI_code.zip
```
     
 - [ ] Extract the files.
 - [ ] Navigate to the folder ```LCD_Module_RPI_code/RaspberryPi/python/example``` and Run "2inch_LCD_test.py"
 - [ ] There maybe a minor bug in the given code, change `Image.open('../pic/LCD_2inch4_1.jpg')` to `Image.open('../pic/LCD_2inch.jpg')`
 - [ ] You will now see an image!
 - [ ] Try to modify the code and use AI tools to help you understand what each part does.

🎉 **Check Point 1**
<br>Show the completion. Also show the SPI inspection **via Analog Discovery (Protocol)**.

---
## 3. SPI - A News Displayer
**Overall, in this part, you will realize a small news displayer system:**  

**Best Level: Auto fetch (100% credit)**
<br>It automatically parses the latest Syracuse University News content from the webpage (headline + a related image), formats it into the screen, and rotately display multiple news items on the LCD.

**Secondary Level: Manual screenshots (50% credit)**
<br>You take manual screenshots of recent SU News, save them as local image files, and rotately display multiple news items on the LCD.

---
 - [ ] The webpage is https://news.syr.edu/news/
 - [ ] Suggestion for accelerating your development:
 <br> You can split the work within your group:
* **Parsing team (Laptop):** Develop and test the webpage parsing code on a personal laptop.
* **Display team (Raspberry Pi):** In parallel, test the LCD display code on the Raspberry Pi
 - [ ] AI tools are allowed in development.
 - [ ] Here is an example I did with manual screenshots:
       
<img src="Pic/lcd_news.jpg" width="600"/>

🎉 **Check Point 2**
<br>Each student will be asked regarding to the implementation and personal contribution     
<br>Carefully disconnect the LCD and properly organize the items before you leave.
