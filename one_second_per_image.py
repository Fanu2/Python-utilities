from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips


def create_video_from_images_with_music(image_folder, music_path, output_video_path, fps=1, duration_per_image=1):
    # Create a list of image file paths
    image_files = [f"{image_folder}/frame_{str(i).zfill(3)}.png" for i in range(31)]  # frame_000.png to frame_030.png

    # Create a video clip from the images
    clip = ImageSequenceClip(image_files, fps=fps)

    # Load the music file
    audio = AudioFileClip(music_path)

    # Set the duration of the video clip to match the audio duration
    clip = clip.set_duration(audio.duration)

    # Set audio to the video clip
    clip = clip.set_audio(audio)

    # Write the video file to disk
    clip.write_videofile(output_video_path, codec='libx264')


# Paths
image_folder = '/home/jasvir/Pictures/transform/resized'
music_path = '/home/jasvir/Pictures/transform/resized/1.mp3'
output_video_path = '/home/jasvir/Pictures/transform/resized/output_video.mp4'

# Create the video
create_video_from_images_with_music(image_folder, music_path, output_video_path)
