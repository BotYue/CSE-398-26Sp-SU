# Week 8 Mon: Speech Recognition

---------------
#### :dizzy: **Lab Date :** Mar 2
#### :alarm_clock: **Due Date :** 2:00 pm Mar 16   
#### :pencil: Every group member must be present for every check point.
-------------------

## 1. Basic Set-up — ```Ultralytics``` and YOLO

- [ ] **Connect to the USB 3.0 of Rasp Pi.**

We have Logitech Brio 100 or Brio 101 webcam.

https://www.amazon.com/Logitech-Webcam-Meetings-Streaming-Built/dp/B0BXGFFSL1




- [ ] **Install Ultralytics**

Go to https://github.com/ultralytics/ultralytics find the installation command.

Always remember to adjust for Pi OS: ```pip3``` and ```--break-system-packages```

```Ultralytics``` automatically installation many other useful Python packages for computer vision. 

- [ ] **Download YOLO26**

Run this Python. It will download the model of YOLO26 nano model
<br> This model is released on Jan 2026.

https://docs.ultralytics.com/models/yolo26/

```python
from ultralytics import YOLO
model = YOLO("yolo26n.pt")
## n is nano model (smallest)
## .pt is the PyTorch format. 
```

- [ ] **Run YOLO26 with Camera Stream**

Run this Python.

```python
import cv2
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small = cv2.resize(frame, (320, 240))     # force 320x240 input
    results = model.predict(small, imgsz=320, verbose=False)  # keep img small

    annotated = results[0].plot()
    cv2.imshow("YOLO USB Cam", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

Place a few objects before camera and see if works!

The objects have to be in one of the 80 categories in https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml 

You can also simply check the 80 categories in Python:

```python
model = YOLO("yolo26n.pt")
print(model.names)
```

<img src="Pic/yolo_cao.jpg" width="500"/>



## 2. **Visual Servoing with YOLO**

In the previous code, add this right below `results = model.predict(small, imgsz=320, verbose=False)`

```python
print(results)
```

Observe what is print out.

Then, change the print to 
```python
results[0].speed
```
and
```python
results[0].boxes
```
Observe what is print out.

