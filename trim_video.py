from moviepy.editor import VideoFileClip


def trim_video(input_video_path, output_video_path, start_time=0, end_time=35):
    # Load the video file
    video = VideoFileClip(input_video_path)

    # Trim the video to the specified time range
    trimmed_video = video.subclip(start_time, end_time)

    # Write the trimmed video to the output file
    trimmed_video.write_videofile(output_video_path, codec='libx264', bitrate='500k')


# Paths
input_video_path = '/home/jasvir/Pictures/transform/resized/output_video.mp4'
output_video_path = '/home/jasvir/Pictures/transform/resized/trimmed_video.mp4'

# Trim the video
trim_video(input_video_path, output_video_path, start_time=0, end_time=35)
