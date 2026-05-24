import os
import shutil
import random

def split_dataset(input_images_folder, output_folder, train_percent=0.85, val_percent=0.10, test_percent=0.05):
    os.makedirs(output_folder, exist_ok=True)

    for cls in os.listdir(input_images_folder):
        class_path = os.path.join(input_images_folder, cls)
        image_files = [f for f in os.listdir(class_path) if f.endswith('.jpg')]
        random.shuffle(image_files)
        total_files = len(image_files)
        train_count = int(total_files * train_percent)
        val_count = int(total_files * val_percent)
        test_count = total_files - train_count - val_count

        train_images = image_files[:train_count]
        val_images = image_files[train_count:train_count + val_count]
        test_images = image_files[train_count + val_count:]

        train_images_path = os.path.join(output_folder, 'train', cls)
        os.makedirs(train_images_path, exist_ok=True)
        for img_file in train_images:
            shutil.copy(os.path.join(input_images_folder, cls, img_file), os.path.join(train_images_path, img_file))

        valid_images_path = os.path.join(output_folder, 'valid', cls)
        os.makedirs(valid_images_path, exist_ok=True)
        for img_file in val_images:
            shutil.copy(os.path.join(input_images_folder, cls, img_file), os.path.join(valid_images_path, img_file))

        test_images_path = os.path.join(output_folder, 'test', cls)
        os.makedirs(test_images_path, exist_ok=True)
        for img_file in test_images:
            shutil.copy(os.path.join(input_images_folder, cls, img_file), os.path.join(test_images_path, img_file))

def main():
    path = r'C:\Users\asasr\Documents\!Институт\2_семестр\Potato_illness_detecter'

    input_images_folder = os.path.join(path, 'Resized_dataset')
    output_folder = os.path.join(path, 'DatasetYOLO')

    split_dataset(input_images_folder, output_folder)

if __name__ == "__main__":
    main()