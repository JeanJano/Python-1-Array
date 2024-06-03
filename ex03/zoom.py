from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(path: str, crop: dict) -> None:
    """
    This function loads an image from a given path, crops it according
    to the given dimensions, and saves the cropped image.
    It also prints the new size of the image in pixels, its new shape,
    and the RGB values for each pixel.

    Parameters:
    path (str): The path to the image file.
    crop (dict): A dictionary with keys 'top', 'bottom', 'left', 'right'
    specifying the dimensions for cropping.

    Returns:
    None

    Raises:
    AssertionError: If crop is not a dictionary, does not have the required
    keys, or the image could not be loaded.
    Exception: For any other exceptions that may occur.
    """
    try:
        assert isinstance(crop, dict), """assertion error: crop should be a
            dictionary"""
        assert all(key in crop for key in
                   ['top', 'bottom', 'left', 'right']), """assertion error:
                   crop should have the keys 'top', 'bottom',
                   'left', 'right'"""

        img = ft_load(path)
        assert img is not None, "assertion error: image should not be None"

        crop_img = img[crop['top']:crop['bottom'], crop['left']:crop['right']]
        plt.imshow(crop_img)
        # plt.show()
        plt.savefig("crop.jpeg")

        print(f"""New size in pixel of the image: x:
              {crop['right'] - crop['left']} y:{crop['bottom']
                                                - crop['top']}""")
        print(f"New shape after slicing: {crop_img.shape}")
        height, width, _ = crop_img.shape
        for y in range(height):
            for x in range(width):
                r, g, b = crop_img[y, x]
                print(f"[{r}, {g}, {b}]")

    except AssertionError as e:
        print(e)

# def main() -> None:
#     crop = {
#         'top': 100,
#         'bottom': 500,
#         'left': 400,
#         'right': 900
#     }
#     ft_zoom("../animal.jpeg", crop)

# if __name__ == "__main__":
#     main()
