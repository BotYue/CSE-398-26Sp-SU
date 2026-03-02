# Week 8 Wed: Computer Vision 2

---------------
#### :dizzy: **Lab Date :** Mar 4
#### :alarm_clock: **Due Date :** 2:00 pm Mar 16   
#### :pencil: Every group member must be present for every check point.
-------------------

## 1. Image Classification Workflow — Fashion MNIST

In this task, we will try the image classification workflow via deep learning. We will go thru the procedures step by step.

We will use **PyTorch** + **Torchvision** as deep vision framework. They are already installed when you installed ```Ultralytics``` 

We will try on a simple dataset -- **Fashion MNIST**.

* Dataset description: https://www.kaggle.com/datasets/zalando-research/fashionmnist
* PyTorch Fashion MNIST Tutorial details: https://pytorch.org/tutorials/beginner/introyt/trainingyt.html

----------------------

- [ ] **Model Training: Follow the PyTorch Fashion MNIST Tutorial and complete the model trainning.**

* Typically, you don't want to train model in embeded devices due to resource constraints.
<br>So, use either your own laptop or Cloud platform to train the model.
<br>I recommend that you just use Google Colab because PyTorch is already there without extra installation.

* You can direct use the code blocks given in the official tutorial.
<br>I personally set the `EPOCHS = 10` instead of `EPOCHS = 5` for better training results (but longer run).

- [ ] **Inference with Real Image**

* Place a fashion item before a background. There are 10 accepted item types. They can be found in previous [kaggle hyperlink](https://www.kaggle.com/datasets/zalando-research/fashionmnist).

* Take a photo of it. Ensure clean background and high contrast between item and background. (I used my phone to take picture)

* Preprocess images to convert them to the same style as Fashion MNIST images. (I used my photo-edit app to crop and filter. Then I upload the image to ChatGPT and ask it to generate code that: "use opencv to preprocess the uploaded image for Fashion MNIST dataset. Ensure clear edge and good contrast." )

* Then, start over a new .py file. Use your previously trained neural networks and perform inference on the images. Also record the inference time.

* Does it predict the correct label?

| **Raw Image** |**Preprocessed then Perform Prediction** |
|---------|---------|
| <img src="Pic/1000028901.jpg" height="350"> | <img src="Pic/Figure_2.png" height="400"> |

```shell
>>> %Run caopredict.py
Predicted Class: Bag
Inference Time: 0.0048 seconds
```

🎉 **Check Point 1**

Show your result. (Can use your laptop or raspberry pi)

------------------
## 2. Real-Time Video Frame Classification  — MobileNet

In the Monday's task, when you run YOLO on Raspberry Pi 5, you may notice the frame rate is relatively low (less than 20 FPS).

Instead of detecting **multiple objects + bounding boxes** (YOLO), we will simplify the problem to recognizing **a single main object** in the camera view.

* **YOLO** is for **object detection**: it finds multiple objects in an image, and outputs **{class + location/bounding box + confidence}**.
* **MobileNet** is for **image classification**: it predicts one label for the whole image, and outputs **{class + confidence}**.

Because classification is simpler than detection, it runs significantly faster on embedded platforms like Raspberry Pi.

---------

- [ ] **Pre-trained MobileNetV3-Large Model**

We will use the pretrained **MobileNetV3-Large** model provided by PyTorch:

[https://docs.pytorch.org/vision/main/models/mobilenetv3.html](https://docs.pytorch.org/vision/main/models/mobilenetv3.html)

The model was published in 2019: https://arxiv.org/abs/1905.02244  . 
<br>It is trained on the **ImageNet-1K dataset**, which contains 1000 object categories.

* Standard naming: https://github.com/pytorch/hub/blob/master/imagenet_classes.txt ; 
* Alternative American-styled naming: https://github.com/anishathalye/imagenet-simple-labels

- [ ] **Optimize for Embedded Device**

Instead of using the default implementation, you should apply a few embedded-friendly optimizations:

* Limit PyTorch CPU threads, leave room for other tasks such as OpenCV pre-processing, Flask streaming, ...
* Use int8 quantization to speed up CPU inference
* Use QNNPACK as the quantized backend (optimized for ARM CPUs)
  
> [!TIP]
> A detailed explanation of these optimizations can be found in the article:
[https://docs.pytorch.org/tutorials/intermediate/realtime_rpi.html](https://docs.pytorch.org/tutorials/intermediate/realtime_rpi.html)
> 
> Note, this article uses MobileNetV2 and doen't use a USB camera, but the same optimization ideas.

The optimized model can be verified using the following code:
  
```python
import torch
from torchvision.models.quantization import mobilenet_v3_large, MobileNet_V3_Large_QuantizedWeights

torch.set_num_threads(2)
torch.backends.quantized.engine = "qnnpack"

# Load quantized V3-Large
weights = MobileNet_V3_Large_QuantizedWeights.DEFAULT
model = mobilenet_v3_large(weights=weights, quantize=True).eval()

# JIT
model = torch.jit.script(model)

print("MobileNetV3-Large INT8 loaded successfully.")
```

* [ ] **Real-Time Video Frame Classification on Raspberry Pi**

Your task is to implement a **real-time video frame classification system** using the **MobileNetV3-Large** model (ImageNet pretrained).

* Use a live USB camera stream on the Raspberry Pi.
* Capture video frames continuously.
* For each video frame:

  * Perform MobileNetV3-Large inference.
  * Compute the Top-1 predicted class label.
  * Compute the corresponding confidence score.
* Overlay the following information directly on the live video stream: 

  * Predicted label
  * Confidence 
  * FPS
  
> [!TIP]
>In Pi OS, the  ```cv2.imshow``` often conflicts with system GUI and may result to an error ```could not find the Qt platform plugin "wayland"``` . If so, you can use Python ```flask``` to display the stream on Pi's browser.
> 
>You can use `cv2.putText` to overlay text.



----------
Here are 3 screenshots of my running (This is using ```flask``` package and display a real-time steam in a browser):

| **Screenshot 1** |**Screenshot 2** |**Screenshot 3** |
|---------|---------|---------|
| <img src="Pic/MN_3.png" height="250"> | <img src="Pic/MN_2.png" height="250"> |<img src="Pic/MN_1.png" height="250"> |

🎉 **Check Point 2**

Each student must present **individually for 30 seconds** to describe personal contributions during this lab.<br>
Each student will be asked a question regarding to implementation.<br>
The other two students in the same group must not assist.<br>
Failure to demonstrate meaningful contribution, or answer questions will result in point loss in the corresponding Markdown submission.
