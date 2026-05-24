from ultralytics import YOLO

model = YOLO("yolo26n-cls.pt")

results = model.train(data="DatasetYOLO", epochs=100, imgsz=640)

model.save("potato.pt")
