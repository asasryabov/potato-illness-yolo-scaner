import sys
from pathlib import Path

from ultralytics.models import YOLO

if len(sys.argv) != 2:
    print(f"Использование: {sys.argv[0]} <файл>")
    sys.exit(1)

image_path = Path(sys.argv[1])
if not image_path.is_file():
    print(f"Файл не найден: {image_path}")
    sys.exit(1)

model = YOLO("potato.pt")
result = model(str(image_path), verbose=False)[0]

if result.probs is None:
    print("Модель не вернула вероятности классов (ожидается classify-модель)")
    sys.exit(1)

class_idx = result.probs.top1
confidence = result.probs.top1conf.item()
class_name = result.names[class_idx]

print(f"Файл: {image_path}")
print(f"Класс: {class_name}")
print(f"Уверенность: {confidence:.4f}")
