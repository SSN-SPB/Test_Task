from PIL import Image, ImageChops



def compare_two_images(image_one, image_two) -> bool:
    base_image = Image.open(image_one)
    base_image = base_image.convert("RGBA")
    test_image = Image.open(image_two)
    test_image = test_image.convert("RGBA")
    # Type your code here
    # return "".join(str(element) for element in a_list[::-1])
    return ImageChops.difference(base_image, test_image)


def main():
    print(compare_two_images("im1.png", "im2.png").getbbox())
    print(compare_two_images("im1.png", "im2v2.png").getbbox())


if __name__ == "__main__":
    main()
