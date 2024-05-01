from PIL import Image

# Load the image
image_path = "microphone imge.png"
image = Image.open(image_path)

# Convert the image to grayscale and resize
image_gray = image.convert("L")
image_gray_resized = image_gray.resize((60, 60))

# Define ASCII characters representing different intensity levels
ascii_chars = "@%#*+=-:. "

# Iterate over each pixel and print corresponding ASCII character
ascii_art = ""
for y in range(image_gray_resized.size[1]):
    for x in range(image_gray_resized.size[0]):
        intensity = image_gray_resized.getpixel((x, y))
        ascii_art += ascii_chars[int(intensity / 256 * len(ascii_chars))]
    ascii_art += "\n"

# Print the ASCII art
print(ascii_art)
