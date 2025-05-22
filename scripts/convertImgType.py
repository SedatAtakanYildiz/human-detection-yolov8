from PIL import Image
import os

input_folder = 'dataset/images'
output_folder = 'dataset/images'

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.webp')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert('RGB')  # RGBA gibi format sorunlarını da önler

        # Yeni dosya adı
        new_filename = os.path.splitext(filename)[0] + '.jpg'
        new_path = os.path.join(output_folder, new_filename)
        img.save(new_path, 'JPEG')

        # Orijinal dosyayı sil
        os.remove(img_path)
        print(f"Converted and removed: {filename}")