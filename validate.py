from ultralytics import YOLO

model = YOLO("potato.pt")

metrics = model.val(data="DatasetYOLO", imgsz=640, batch=64)

print(f"Fitness: {metrics.fitness:.4f}")
print(f"Top1: {metrics.top1:.4f}")

print(metrics.results_dict.keys())
