from ctypes import Array
# from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_rotate(image: Array, angle: float) -> None:
    """
    This function rotates an image by a given angle and saves the rotated
    image.
    It also prints the new shape of the image and the RGB values for each
    pixel.

    Parameters:
    image (Array): The image to be rotated as a 3D array (height, width, RGB).
    angle (float): The angle by which to rotate the image in degrees.

    Returns:
    None

    Raises:
    AssertionError: If the image is not a 3D array or the angle is not a float.
    Exception: For any other exceptions that may occur.
    """
    angle_rad = np.radians(angle)  # Convert angle to radians

    height, width, _ = image.shape  # Get the shape of the image

    # Calculate the center of the image
    center_x = width // 2
    center_y = height // 2

    # Create a new image with the same shape as the original image
    rotated_image = np.zeros_like(image)

    for y in range(height):
        for x in range(width):
            # Calculate the coordinates relative to the center
            x_rel = x - center_x
            y_rel = y - center_y

            # Rotate the coordinates
            new_x = (x_rel * np.cos(angle_rad) - y_rel * np.sin(angle_rad))
            + center_x
            new_y = (x_rel * np.sin(angle_rad) + y_rel * np.cos(angle_rad))
            + center_y

            # Check if the new coordinates are within the bounds
            if 0 <= new_x < width and 0 <= new_y < height:
                rotated_image[int(new_y), int(new_x)] = image[y, x]

    plt.imshow(rotated_image)
    # plt.show()
    plt.savefig("rotate.jpeg")

    print(f"new shape after transpose: {rotated_image.shape}")
    height, width, _ = rotated_image.shape
    for y in range(height):
        for x in range(width):
            r, g, b = rotated_image[y, x]
            print(f"[{r}, {g}, {b}]")


# def main() -> None:
#     img = ft_load("../animal.jpeg")
#     if img is not None:
#         ft_rotate(img, -90)


# if __name__ == "__main__":
#     main()
