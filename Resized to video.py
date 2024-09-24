from moviepy.editor import ImageSequenceClip
from PIL import Image  # Add this import
import os


def create_video_from_images(image_dir, output_video_path, fps=24):
    """Create a video from the images in the specified directory."""
    image_files = [os.path.join(image_dir, f) for f in sorted(os.listdir(image_dir)) if f.endswith('.png')]

    if not image_files:
        print("No images found for video creation.")
        return

    # Print sizes of all images to debug
    for image_file in image_files:
        with Image.open(image_file) as img:
            print(f"Image {image_file} size: {img.size}")

    if not check_image_sizes(image_dir):
        print("Cannot create video. Images are not all the same size.")
        return

    print(f"Creating video from {len(image_files)} images.")
    try:
        clip = ImageSequenceClip(image_files, fps=fps)
        clip.write_videofile(output_video_path, codec="libx264")
        print(f"Video saved as {output_video_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_image_sizes(image_dir):
    """Check if all images in the directory are of the same size."""
    sizes = set()
    for file_name in os.listdir(image_dir):
        if file_name.endswith('.png'):
            image_path = os.path.join(image_dir, file_name)
            with Image.open(image_path) as img:
                sizes.add(img.size)
                print(f"Image {image_path} size: {img.size}")

    if len(sizes) == 1:
        print(f"All images are of size: {sizes.pop()}")
        return True
    else:
        print("Image sizes are inconsistent!")
        return False


def main():
    resized_image_dir = '/home/jasvir/Pictures/transform/resized'
    output_video_path = '/home/jasvir/Pictures/transform/transition.mp4'

    create_video_from_images(resized_image_dir, output_video_path)


if __name__ == '__main__':
    main()
