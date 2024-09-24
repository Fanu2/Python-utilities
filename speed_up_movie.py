from moviepy.editor import VideoFileClip


def speed_up_video(input_video_path, output_video_path, target_duration):
    # Load the video clip
    clip = VideoFileClip(input_video_path)

    # Calculate the speed-up factor
    original_duration = clip.duration
    speed_up_factor = original_duration / target_duration

    # Speed up the clip
    sped_up_clip = clip.fx(lambda c: c.set_duration(c.duration / speed_up_factor))

    # Write the sped-up video to the output file
    sped_up_clip.write_videofile(output_video_path, codec='libx264')


# Paths
input_video_path = '/home/jasvir/Pictures/transform/resized/1.mp4'
output_video_path = '/home/jasvir/Pictures/transform/resized/1_sped_up.mp4'
target_duration = 30  # Target duration in seconds

# Speed up the video
speed_up_video(input_video_path, output_video_path, target_duration)
