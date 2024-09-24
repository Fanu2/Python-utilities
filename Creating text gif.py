from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip


def create_image_with_text(text, font_path, text_color, background_color, image_size, output_path):
    width, height = image_size
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    font_size = 100
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, font=font, fill=text_color)
    image.save(output_path)
    return output_path


def main():
    text = "Love u Jodha"
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    background_color = (245, 245, 220)
    image_size = (800, 400)
    frame_duration = 0.5  # seconds per frame
    output_gif = "love_u_jodha.gif"
    output_video = "/home/jasvir/Pictures/Jodha/love_u_jodha.mp4"

    colors = [(255, 0, 0), (0, 128, 0), (0, 0, 255), (255, 165, 0), (128, 0, 128)]
    image_files = []

    for i, color in enumerate(colors):
        output_path = f"frame_{i}.png"
        image_files.append(create_image_with_text(text, font_path, color, background_color, image_size, output_path))

    clip = ImageSequenceClip(image_files, fps=1 / frame_duration)
    clip.write_gif(output_gif, fps=1 / frame_duration)
    clip.write_videofile(output_video, fps=1 / frame_duration)


if __name__ == '__main__':
    main()
