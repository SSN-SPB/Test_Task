from PIL import Image

original = Image.open("actual_screenshot.png").convert("RGBA")
masked = Image.open("actual_screenshot_with_added_mask.png").convert("RGBA")

orig_pixels = original.load()
mask_pixels = masked.load()
width, height = original.size

result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
result_pixels = result.load()

masked_count = 0
for y in range(height):
    for x in range(width):
        r1, g1, b1, _ = orig_pixels[x, y]
        r2, g2, b2, _ = mask_pixels[x, y]
        if (r1, g1, b1) != (r2, g2, b2):
            result_pixels[x, y] = (r2, g2, b2, 255)
            masked_count += 1

result.save("found_difference_mask_image.png")
print(f"found_difference_mask_image.png saved — masked pixels: {masked_count}, total pixels: {width * height}")
