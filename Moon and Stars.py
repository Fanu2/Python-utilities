from PIL import Image, ImageDraw
import math

# Load images
main_image_path = "/home/jasvir/Pictures/Jodha/1.png"
star_images_paths = [
    "/home/jasvir/Pictures/Jodha/2.png",
    "/home/jasvir/Pictures/Jodha/3.png",
    "/home/jasvir/Pictures/Jodha/4.png",
    "/home/jasvir/Pictures/Jodha/5.png",
    "/home/jasvir/Pictures/Jodha/6.png",
    "/home/jasvir/Pictures/Jodha/7.png"
]

main_image = Image.open(main_image_path)
star_images = [Image.open(path) for path in star_images_paths]

# Create a new blank image with white background
output_size = (1080, 1920)  # Mobile resolution
output_image = Image.new("RGB", output_size, "black")

# Resize and mask the main image (moon)
main_image_size = (300, 300)  # Adjust size as needed
main_image = main_image.resize(main_image_size)

mask = Image.new("L", main_image_size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + main_image_size, fill=255)
main_image.putalpha(mask)

main_image_position = (
    (output_size[0] - main_image_size[0]) // 2,
    (output_size[1] - main_image_size[1]) // 2
)
output_image.paste(main_image, main_image_position, main_image)

# Resize and mask star images
star_size = (100, 100)  # Adjust size as needed
for i, star_image in enumerate(star_images):
    star_image = star_image.resize(star_size)

    star_mask = Image.new("L", star_size, 0)
    star_draw = ImageDraw.Draw(star_mask)
    star_draw.ellipse((0, 0) + star_size, fill=255)
    star_image.putalpha(star_mask)

    # Calculate position for each star
    angle = 2 * math.pi * i / len(star_images)
    radius = 400  # Distance from the center
    x = int(output_size[0] // 2 + radius * math.cos(angle) - star_size[0] // 2)
    y = int(output_size[1] // 2 + radius * math.sin(angle) - star_size[1] // 2)

    output_image.paste(star_image, (x, y), star_image)

# Save the output image
output_image.save("/home/jasvir/Pictures/Jodha/output_mobile.png")
