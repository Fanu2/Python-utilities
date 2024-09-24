from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips
from PIL import Image
import os


def resize_images(image_folder, output_folder, size=(640, 480)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_file in os.listdir(image_folder):
        if image_file.endswith('.png'):
            img_path = os.path.join(image_folder, image_file)
            output_path = os.path.join(output_folder, image_file)
            with Image.open(img_path) as img:
                img = img.resize(size)
                img.save(output_path)
            print(f"Resized and saved: {output_path}")


def check_image_sizes(image_files):
    sizes = set()
    for image_file in image_files:
        with Image.open(image_file) as img:
            sizes.add(img.size)
            print(f"Size of {image_file}: {img.size}")
    if len(sizes) > 1:
        raise ValueError(f"Images have different sizes: {sizes}")


def create_looping_video(image_folder, music_path, output_video_path, duration=30, fps=1):
    resized_image_folder = os.path.join(image_folder, 'resized')
    resize_images(image_folder, resized_image_folder)

    # Get list of image files in the resized folder
    image_files = sorted(
        [os.path.join(resized_image_folder, f) for f in os.listdir(resized_image_folder) if f.endswith('.png')])

    if not image_files:
        raise ValueError("No images found in the specified folder.")

    # Check if all images are the same size
    check_image_sizes(image_files)

    # Create a video clip from the images
    clip = ImageSequenceClip(image_files, fps=fps)

    # Calculate the duration each image should be displayed
    image_duration = duration / len(image_files)

    # Set each image to be displayed for the calculated duration
    clip = clip.set_duration(image_duration)

    # Load the music file
    audio = AudioFileClip(music_path)

    # Adjust the duration of the clip to fit the music
    clip = clip.set_duration(duration)
    audio = audio.subclip(0, duration)  # Trim the audio to match the video duration
    clip = clip.set_audio(audio)

    # Create the final video with looping
    repeated_clips = [clip] * ((duration // clip.duration) + 1)
    final_clip = concatenate_videoclips(repeated_clips, method='compose').subclip(0,
                                                                                  duration)  # Ensure the final clip is exactly 30 seconds

    # Write the video file to disk
    final_clip.write_videofile(output_video_path, codec='libx264', bitrate='500k')


# Paths
image_folder = '/home/jasvir/Pictures/transform'
music_path = '/home/jasvir/Pictures/transform/resized/1.mp3'
output_video_path = '/home/jasvir/Pictures/transform/resized/output_video.mp4'

# Create the looping video
create_looping_video(image_folder, music_path, output_video_path, duration=30)
