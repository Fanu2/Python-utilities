from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text, font_path, output_path):
    # Image dimensions
    width, height = 800, 400
    background_color = (245, 245, 220)  # Light beige background
    text_color = (0, 128, 0)  # Green text

    # Create a new image with the specified background color
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load the font and calculate the text size
    font_size = 100
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the position for the text to be centered
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Add the text to the image
    draw.text((x, y), text, font=font, fill=text_color)

    # Save the image
    image.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    text = "Love u Fanu"
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Path to the font file
    output_path = "/home/jasvir/Pictures/Fanu/Fanu_image2.png"  # Output file path

    create_image_with_text(text, font_path, output_path)

if __name__ == '__main__':
    main()
