import torch
import cv2

# -----------------------------------------------------
# 1. Load YOLOv5 model (small, fast version)
#    torch.hub.load automatically downloads if missing
# -----------------------------------------------------
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# -----------------------------------------------------
# 2. Open webcam
#    0 = default laptop camera
# -----------------------------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Press 'q' to quit camera")

# -----------------------------------------------------
# 3. Loop to read the camera feed
# -----------------------------------------------------
while True:
    ret, frame = cap.read()  # read a single frame

    if not ret:
        print("Failed to grab frame")
        break

    # -------------------------------------------------
    # 4. Run YOLO detection on the frame
    # -------------------------------------------------
    results = model(frame)

    # -------------------------------------------------
    # 5. Convert YOLO output into an image with boxes
    # -------------------------------------------------
    annotated_frame = results.render()[0]  # returns list → take first image

    # -------------------------------------------------
    # 6. Display frame on screen
    # -------------------------------------------------
    cv2.imshow("YOLOv5 Live Detection", annotated_frame)

    # -------------------------------------------------
    # 7. Press "q" to quit
    # -------------------------------------------------
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------------------------------
# 8. Cleanup when closing program
# -----------------------------------------------------
cap.release()
cv2.destroyAllWindows()
