from PIL import Image
import os

cnt = 0
path = r'C:\Users\asasr\Documents\!Институт\2_семестр\Potato_illness_detecter'

for cls in os.listdir(os.path.join(path, "Dataset")):
    os.makedirs(os.path.join(path, "Resized_dataset", cls), exist_ok=True)
    class_path = os.path.join(path, "Dataset", cls)
    print(f"Resize: {class_path}")
    for item in os.listdir(class_path):
        img_path = os.path.join(class_path, item)
        if os.path.isfile(img_path):
            im = Image.open(img_path)
            # f, e = os.path.splitext(item)
            imResize = im.resize((224,224), Image.LANCZOS)
            resized_img_path = os.path.join(path, "Resized_dataset", cls, item)
            imResize.save(resized_img_path, 'JPEG', quality=90)
