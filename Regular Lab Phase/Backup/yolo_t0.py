from ultralytics import YOLO
model = YOLO("yolo26n.pt")
## n is nano model (smallest)
## .pt is the PyTorch format. 
## YOLO also has implementations in other frameworks beyond PyTorch.