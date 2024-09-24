import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip

def apply_light_effects(image):
    # Light effect functions
    effects = [
        lambda img: ImageEnhance.Brightness(img).enhance(1.2),  # Slightly increase brightness
        lambda img: ImageEnhance.Contrast(img).enhance(1.2),    # Slightly increase contrast
        lambda img: img.filter(ImageFilter.GaussianBlur(2)),    # Slight blur for softening
        lambda img: ImageOps.colorize(img.convert('L'), '#ffffff', '#ffd700'),  # Colorize with light effect
        lambda img: ImageEnhance.Color(img).enhance(1.5),       # Increase color saturation
        lambda img: img.filter(ImageFilter.SMOOTH),             # Smooth filter
        lambda img: img.filter(ImageFilter.SHARPEN),            # Sharpen filter
        lambda img: img.filter(ImageFilter.EDGE_ENHANCE),       # Edge enhance filter
        lambda img: ImageEnhance.Brightness(img).enhance(1.5),  # Increase brightness more
        lambda img: img.filter(ImageFilter.BLUR)                # Apply blur filter
    ]
    return effects

def create_images(output_dir, base_image_path):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_image = Image.open(base_image_path).convert("RGB")
    effects = apply_light_effects(base_image)

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
    output_video_path = os.path.join(image_dir, "output2.mp4")

    create_images(image_dir, base_image_path)
    create_video_from_images(image_dir, audio_path, output_video_path)

if __name__ == '__main__':
    main()
