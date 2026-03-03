import cv2
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small = cv2.resize(frame, (320, 240))     # force 320x240 input
    results = model.predict(small, imgsz=320, verbose=False)  # keep imgsz small

    annotated = results[0].plot()
    cv2.imshow("YOLO USB Cam", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()