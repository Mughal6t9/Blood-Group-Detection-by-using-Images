from ultralytics import YOLO
import os

checkpoint_path = r"E:\Blood Group Detection (Images)\runs\detect\train\weights\last.pt"

if os.path.exists(checkpoint_path):
    print("Resuming training from last checkpoint...")
    model = YOLO(checkpoint_path)
    results = model.train(resume=True)
else:
    print("Starting new training from yolov8n.pt...")
    model = YOLO("yolov8n.pt")
    results = model.train(
        data=r"E:\Blood Group Detection (Images)\Yolo Model\data.yaml",
        epochs=50,
        imgsz=640
    )

results.save()
results.show()
