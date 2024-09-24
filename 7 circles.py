from PIL import Image, ImageDraw
import numpy as np
import math


def make_circular_mask(size):
    """Create a circular mask."""
    w, h = size
    mask = Image.new('L', (w, h), 0)
    draw = ImageDraw.Draw(mask)
    center = (w // 2, h // 2)
    radius = min(center)
    draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=255)
    return mask


def create_composite_image(main_image_path, surrounding_images_paths, output_path):
    """Create a composite image with a central image and surrounding images."""
    # Load and prepare the main image
    main_image = Image.open(main_image_path).resize((300, 300))
    main_mask = make_circular_mask(main_image.size)
    main_image.putalpha(main_mask)

    # Number of surrounding images
    num_surrounding_images = len(surrounding_images_paths)
    radius = 350  # Adjusted radius for better frame fitting
    angle_step = 2 * math.pi / num_surrounding_images

    # Create a new image for the final composition
    composite_size = (1280, 720)
    composite_image = Image.new('RGBA', composite_size, (255, 255, 255, 0))

    # Paste the main image in the center
    composite_image.paste(main_image, (composite_size[0] // 2 - main_image.width // 2,
                                       composite_size[1] // 2 - main_image.height // 2), main_image)

    # Add surrounding images
    for i, img_path in enumerate(surrounding_images_paths):
        img = Image.open(img_path).resize((100, 100))  # Resize the surrounding images
        img_mask = make_circular_mask(img.size)
        img.putalpha(img_mask)

        angle = i * angle_step
        x = int(composite_size[0] // 2 + radius * math.cos(angle) - img.width // 2)
        y = int(composite_size[1] // 2 + radius * math.sin(angle) - img.height // 2)

        # Adjust the y-position to ensure top and bottom images are visible
        if angle in [0, math.pi]:  # Top and bottom positions
            y += 30  # Adjust this value as needed to fit within the frame

        composite_image.paste(img, (x, y), img)

    # Save the final composite image
    composite_image.save(output_path)


# Paths
main_image_path = '/home/jasvir/Pictures/Jodha/1.png'
surrounding_images_paths = [f'/home/jasvir/Pictures/Jodha/{i}.png' for i in range(2, 8)]  # Six images
output_path = '/home/jasvir/Pictures/Jodha/composite_image1.png'

# Create the composite image
create_composite_image(main_image_path, surrounding_images_paths, output_path)
