import os
from PIL import Image

def resize_images(image_dir, output_dir, size=(680, 680)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(image_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(image_dir, filename)
            with Image.open(image_path) as img:
                img = img.resize(size, Image.ANTIALIAS)
                output_path = os.path.join(output_dir, filename)
                img.save(output_path)
                print(f"Resized and saved {filename} to {size}")

def main():
    input_dir = "/home/jasvir/Pictures/transform"
    output_dir = "/home/jasvir/Pictures/transform/resized"
    resize_images(input_dir, output_dir)

if __name__ == '__main__':
    main()
