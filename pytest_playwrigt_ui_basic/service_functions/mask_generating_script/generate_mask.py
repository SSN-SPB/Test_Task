from PIL import Image, ImageChops

original = Image.open("actual_demo.png").convert("RGBA")
masked = Image.open("actual_with_applied_mask_demo.png").convert("RGBA")

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
            result_pixels[x, y] = (r2, g2, b2, 255)  # opaque mask color
            masked_count += 1
        # else: stays (0, 0, 0, 0) — transparent

result.save("mask_image.png")
print(f"mask_image.png saved — masked pixels: {masked_count}, total pixels: {width * height}")

# Verify: apply mask back to original and compare with the pre-masked file
initial_image = Image.open("actual_demo.png").convert("RGBA")
composed = Image.alpha_composite(initial_image, result)
composed.save("initial_image_with_applied_mask_demo.png")
print("Verification image saved: initial_image_with_applied_mask_demo.png")
