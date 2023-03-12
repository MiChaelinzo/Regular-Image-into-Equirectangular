import os
from PIL import Image

def convert_to_equirectangular(image_path, width, height):
    # Open the image
    im = Image.open(image_path)

    # Resize the image to the desired width and height
    im = im.resize((width, height))

    # Create a new image with the same width and height, and white background
    eqr_image = Image.new('RGB', (width, height), (255, 255, 255))

    # Map the pixels from the original image onto the equirectangular image
    for x in range(width):
        for y in range(height):
            lon = (x / width) * 360 - 180
            lat = (y / height) * 180 - 90
            pixel = im.getpixel((x, y))
            eqr_x = int(((lon + 180) / 360) * width)
            eqr_y = int(((lat + 90) / 180) * height)
            eqr_image.putpixel((eqr_x, eqr_y), pixel)

    # Save the equirectangular image in the same directory as the original image
    output_path = os.path.splitext(image_path)[0] + '_equirectangular.jpg'
    eqr_image.save(output_path)

# Example usage
image_path = 'C:\\Users\\micha\\Downloads\\cyberpunk-2077-grimes-1.png'
width = 2048
height = 1024

convert_to_equirectangular(image_path, width, height)
