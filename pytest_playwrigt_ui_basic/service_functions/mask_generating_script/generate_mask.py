from PIL import Image

# convert both images to RGBA mode to ensure they have an alpha channel
# to be proceessed by Image module
original = Image.open("actual_screenshot.png").convert("RGBA")
masked = Image.open("actual_screenshot_with_added_mask.png").convert("RGBA")

# load the pixel data for both images
orig_pixels = original.load()
mask_pixels = masked.load()
# get the dimensions of the initial image (width and height)
# script expects that the original and masked images have the same dimensions
width, height = original.size
# create a new image to store the result of the comparison
result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
# load the pixel data for the result image
result_pixels = result.load()

# iterate over each pixel and compare the original and masked images
masked_count = 0
for y in range(height):
    for x in range(width):
        r1, g1, b1, _ = orig_pixels[x, y]
        r2, g2, b2, _ = mask_pixels[x, y]
        # if the pixels are is different,
        # set the pixel from mask image into the result image
        if (r1, g1, b1) != (r2, g2, b2):
            result_pixels[x, y] = (r2, g2, b2, 255)
            masked_count += 1
# if there are any differences found,
# print a message indicating that differences were found
if masked_count != 0:
    print("The difference is found")

# save the result with the difference between images to a file
result.save("created_mask_image.png")

