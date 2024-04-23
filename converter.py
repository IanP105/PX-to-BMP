from PIL import Image

def read_px_file(file_path):
    with open(file_path, 'r') as file:
        data = eval(file.read())
    return data

def create_bmp_from_px(px_data, output_file, wrap_every):
    # Calculate the width and height based on the number of RGB values
    width = len(px_data)

    # Calculate the new width and height based on wrap_every
    new_width = wrap_every
    new_height = (width + wrap_every - 1) // wrap_every

    # Create a new image with the determined width and height
    img = Image.new('RGB', (new_width, new_height))

    # Set pixel values
    for x in range(width):
        r, g, b = px_data[x]
        img.putpixel((x % new_width, x // new_width), (int(r * 255), int(g * 255), int(b * 255)))

    # Save the image as a .bmp file
    img.save(output_file + ".bmp")
    print(f"Image saved as {output_file}.bmp")

if __name__ == "__main__":
    input_file = "vga.px"  # Update the input file path
    output_file = "output"  # Update the output file path
    wrap_every = 536  # Define the number of pixels after which the image should wrap
    px_data = read_px_file(input_file)
    create_bmp_from_px(px_data, output_file, wrap_every)
