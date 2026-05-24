import numpy as np
from ultralytics.models import YOLO

model = YOLO("potato.pt")

metrics = model.val(data="DatasetYOLO", imgsz=640, batch=64)

cm = metrics.confusion_matrix
matrix = cm.matrix[
    : cm.nc, : cm.nc
]  # обрезаем матрицу только для классов, без пустых ячеек (была 8х8 с пустым столбцом и строкой   )
tp = np.diag(matrix)
fp = matrix.sum(axis=1) - tp  # сколько было false positive предсказаний
fn = matrix.sum(axis=0) - tp  # сколько было false negative предсказаний
precision = tp / (tp + fp + 1e-9)  # 1e-9 что бы не делить на 0
recall = tp / (tp + fn + 1e-9)
f1 = 2 * precision * recall / (precision + recall + 1e-9)

print(f"\nPrecision: {precision.mean():.4f}")
print(f"\nRecall: {recall.mean():.4f}")
print(f"\nF1: {f1.mean():.4f}")

print("\nPer class:")
for i, name in cm.names.items():
    print(f"  {name:12} P={precision[i]:.4f}  R={recall[i]:.4f}  F1={f1[i]:.4f}")
