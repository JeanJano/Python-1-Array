from ctypes import Array
import imageio.v2 as imageio


def ft_load(path: str) -> Array:
    """
    This function loads an image from a given path and prints its shape and
    RGB values for each pixel.

    Parameters:
    path (str): The path to the image file.

    Returns:
    Array: The loaded image as a 3D array (height, width, RGB).

    Raises:
    FileNotFoundError: If the image file does not exist at the given path.
    ValueError: If the image file is not readable or not a valid image file.
    Exception: For any other exceptions that may occur.
    """
    try:
        img = imageio.imread(path)
        print(f"The shape of the image is: {img.shape}")

        height, width, _ = img.shape
        for y in range(height):
            for x in range(width):
                r, g, b = img[y, x]
                print(f"[{r}, {g}, {b}]")

        return img

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
