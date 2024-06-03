from ctypes import Array
# from load_image import ft_load
# import matplotlib.pyplot as plt


def ft_invert(img: Array) -> Array:
    """
    This function inverts the colors of an image by subtracting the RGB values
    of each pixel from 255.

    Parameters:
    img (Array): The image to be inverted as a 3D array (height, width, RGB).

    Returns:
    Array: The inverted image as a 3D array (height, width, RGB).
    """
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            img[y, x] = [255 - r, 255 - g, 255 - b]
    return img


def ft_red(img: Array) -> Array:
    """
    This function applies a red filter to an image by setting the green and
    blue values of each pixel to 0.

    Parameters:
    img (Array): The image to be filtered as a 3D array (height, width, RGB).

    Returns:
    Array: The filtered image as a 3D array (height, width, RGB).
    """
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            img[y, x] = [r, 0, 0]
    return img


def ft_green(img: Array) -> Array:
    """
    This function applies a green filter to an image by setting the red and
    blue values of each pixel to 0.

    Parameters:
    img (Array): The image to be filtered as a 3D array (height, width, RGB).

    Returns:
    Array: The filtered image as a 3D array (height, width, RGB).
    """
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            img[y, x] = [0, g, 0]
    return img


def ft_blue(img: Array) -> Array:
    """
    This function applies a blue filter to an image by setting the red and
    green values of each pixel to 0.

    Parameters:
    img (Array): The image to be filtered as a 3D array (height, width, RGB).

    Returns:
    Array: The filtered image as a 3D array (height, width, RGB).
    """
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            img[y, x] = [0, 0, b]
    return img


def ft_grayscale(img: Array) -> Array:
    """
    This function converts an image to grayscale by setting the RGB values of
    each pixel to the weighted average of the original RGB values.

    Parameters:
    img (Array): The image to be converted as a 3D array (height, width, RGB).

    Returns:
    Array: The grayscale image as a 3D array (height, width, RGB).
    """
    height, width, _ = img.shape
    for y in range(height):
        for x in range(width):
            r, g, b = img[y, x]
            # 0.2126, 0.7152, and 0.0722 are the standard coefficients used
            # in the luminosity method for converting a color image to
            # grayscale.
            gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            img[y, x] = [gray, gray, gray]
    return img


# def main() -> None:
#     img = ft_load("../landscape.jpg")
#     # img = ft_invert(img)
#     # img = ft_red(img)
#     # img = ft_green(img)
#     # img = ft_blue(img)
#     img = ft_grayscale(img)

#     plt.imshow(img)
#     # plt.show()
#     plt.savefig("pimp.jpeg")


# if __name__ == "__main__":
#     main()
