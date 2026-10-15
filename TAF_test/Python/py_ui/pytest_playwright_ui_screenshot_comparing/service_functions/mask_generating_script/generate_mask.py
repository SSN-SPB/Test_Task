from pathlib import Path

from PIL import Image


def generate_mask(
    original_path: str | Path,
    marked_path: str | Path,
    output_path: str | Path,
) -> int:
    """
    Generate a mask image by comparing the original and marked images.
    The mask image will highlight the differences between the two images.

    Args:
        original_path (str | Path): Path to the original image.
        marked_path (str | Path): Path to the marked image.
        output_path (str | Path): Path to save the generated mask image.

    Returns:
        int: The number of pixels that differ between the two images.
    """

    # convert both images to RGBA mode to ensure they have an alpha channel
    # to be processed by Image module
    original = Image.open(original_path).convert("RGBA")
    masked = Image.open(marked_path).convert("RGBA")

    # load the pixel data for both images
    orig_pixels = original.load()
    mask_pixels = masked.load()
    # check if the dimensions of the original and masked images are the same
    # it is mandatory that the original and masked images
    # have the same dimensions
    if original.size != masked.size:
        raise ValueError(
            f"The difference of sizes is found: "
            f"{original.size} != {masked.size}"
        )

    # get the dimensions of the image (width and height)
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
            # set the pixel into the result image
            if (r1, g1, b1) != (r2, g2, b2):
                result_pixels[x, y] = (r2, g2, b2, 255)
                masked_count += 1
    # print message if there are any differences found,
    if masked_count != 0:
        print("The difference is found")
        print(f"Changed pixels: {masked_count}")

        # save the result with the difference between images to a file
        result.save(output_path)
        print(f"Mask saved to {output_path}")
        return masked_count
    print("The difference is not found")
    print(f"Changed pixels: {masked_count}")
    return masked_count


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
try:
    generate_mask(
        script_dir / "actual_screenshot.png",
        script_dir / "actual_screenshot_with_added_mask.png",
        script_dir / "created_mask_image.png",
    )
except ValueError as ve:
    print(f"Different dimensions of screenshots are not allowed. {ve}")
