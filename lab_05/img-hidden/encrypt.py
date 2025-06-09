import sys
from PIL import Image

def encode_image(image_path, message):
    # Open the image
    img = Image.open(image_path)

    width, height = img.size
    pixel_index = 0
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Add a "delimiter" to mark the end of the message
    binary_message += '11111111111111110'

    data_index = 0

    # Iterate through the image pixels
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))

            for color_channel in range(3):  # We only modify RGB, not alpha
                if data_index < len(binary_message):
                    # Modify the least significant bit of the pixel
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

            # Update the pixel with the new values
            img.putpixel((col, row), tuple(pixel))

            # If we've encoded the entire message, exit the loop
            if data_index >= len(binary_message):
                break

        if data_index >= len(binary_message):
            break

    # Save the encoded image
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]

    encode_image(image_path, message)

# Corrected the check to ensure the script runs only if it's the main program
if __name__ == "__main__":
    main()
