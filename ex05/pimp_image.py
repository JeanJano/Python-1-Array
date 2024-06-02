from ctypes import Array
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(img: Array) -> Array:
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            img[y, x] = [255 - r, 255 - g, 255 - b]
    return img


def ft_red(img: Array) -> Array:
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            img[y, x] = [r, 0, 0]
    return img


def ft_green(img: Array) -> Array:
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            img[y, x] = [0, g, 0]
    return img


def ft_blue(img: Array) -> Array:
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            img[y, x] = [0, 0, b]
    return img


def ft_grayscale(img: Array) -> Array:
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            # 0.2126, 0.7152, and 0.0722 are the standard coefficients used in the luminosity method for converting a color image to grayscale.
            gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            img[y, x] = [gray, gray, gray]
    return img


def main() -> None:
    img = ft_load("../landscape.jpg")
    # img = ft_invert(img)
    # img = ft_red(img)
    # img = ft_green(img)
    # img = ft_blue(img)
    img = ft_grayscale(img)

    plt.imshow(img)
    # plt.show()
    plt.savefig("pimp.jpeg")


if __name__ == "__main__":
    main()
