import os
import shutil
import random

# Mevcut dosya yolları (senin şu anki birleşik veri klasörlerin)
images_dir = 'dataset/images'
labels_dir = 'dataset/labels'

# Çıktı yolları (YOLO formatına göre)
output_base = 'dataset'  # klasör yapısı buna göre oluşur
train_ratio = 0.8

# Tüm image dosyalarını al (jpg veya png olabilir)
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(image_files)

# Split işlemi
split_index = int(len(image_files) * train_ratio)
train_files = image_files[:split_index]
val_files = image_files[split_index:]

def copy_files(file_list, split_type):
    for file_name in file_list:
        # Klasör oluştur
        os.makedirs(os.path.join(output_base, 'images', split_type), exist_ok=True)
        os.makedirs(os.path.join(output_base, 'labels', split_type), exist_ok=True)

        # Görseli kopyala
        shutil.copy(
            os.path.join(images_dir, file_name),
            os.path.join(output_base, 'images', split_type, file_name)
        )

        # Label dosyasını kopyala
        label_name = os.path.splitext(file_name)[0] + '.txt'
        shutil.copy(
            os.path.join(labels_dir, label_name),
            os.path.join(output_base, 'labels', split_type, label_name)
        )

copy_files(train_files, 'train')
copy_files(val_files, 'val')

print(f"Train: {len(train_files)} images")
print(f"Val: {len(val_files)} images")