import os
from PIL import Image, ImageEnhance, ImageFilter
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip

def create_images(output_dir, base_image_path):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_image = Image.open(base_image_path).convert("RGB")  # Ensure the base image is in RGB mode
    effects = [
        lambda img: img.filter(ImageFilter.GaussianBlur(5)),
        lambda img: ImageEnhance.Contrast(img).enhance(2),
        lambda img: ImageEnhance.Brightness(img).enhance(2),
        lambda img: ImageEnhance.Color(img).enhance(2),
        lambda img: img.rotate(45),
        lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),
        lambda img: img.filter(ImageFilter.DETAIL),
        lambda img: img.convert("L").convert("RGB"),  # Convert to grayscale and then back to RGB
        lambda img: img.filter(ImageFilter.EMBOSS).convert("RGB"),  # Ensure embossed image is in RGB mode
        lambda img: img.filter(ImageFilter.CONTOUR).convert("RGB")  # Ensure contoured image is in RGB mode
    ]

    for i, effect in enumerate(effects):
        new_image = effect(base_image)
        new_image_path = os.path.join(output_dir, f"{i+1}.jpg")
        new_image.save(new_image_path)

def create_video_from_images(image_dir, audio_path, output_video_path, fps=24):
    image_files = [os.path.join(image_dir, f"{i+1}.jpg") for i in range(10)]
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration
    image_duration = audio_duration / 10

    clips = [ImageClip(img).set_duration(image_duration).set_fps(fps) for img in image_files]
    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio_clip)
    video.write_videofile(output_video_path, codec="libx264", audio_codec="aac", fps=fps)

def main():
    image_dir = "/home/jasvir/Pictures/Jodha1"
    base_image_path = os.path.join(image_dir, "1.jpg")
    audio_path = os.path.join(image_dir, "1.mp3")
    output_video_path = os.path.join(image_dir, "output.mp4")

    create_images(image_dir, base_image_path)
    create_video_from_images(image_dir, audio_path, output_video_path)

if __name__ == '__main__':
    main()
